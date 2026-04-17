import os, json, subprocess, sys, re
from shared.board import render_board_table

STATE_FILE = "game_state.json"
SANDBOX_FILE = "current_state.json"

def main():
    issue_title = os.environ.get("GITHUB_EVENT_PATH")
    if issue_title:
        with open(issue_title, 'r') as f:
            event = json.load(f)
            issue_title = event.get("issue", {}).get("title", "")
    else:
        # Fallback for manual testing if needed
        issue_title = os.environ.get("ISSUE_TITLE", "")

    # Regex: Language: Tic-Tac-Toe: Put A1
    # Regex: Language: Tic-Tac-Toe: Reset
    match = re.match(r"(.*?):\s*Tic-Tac-Toe:\s*(Put\s+([A-C][1-3])|Reset)", issue_title, re.IGNORE_CASE)
    if not match:
        print(f"Invalid issue title: {issue_title}")
        sys.exit(0)

    lang_name = match.group(1).strip()
    lang_key = lang_name.lower().replace("#", "sharp").replace("+", "plus").replace("cpp", "cpplus")
    # Mapping fix for C++
    if "c++" in lang_name.lower(): lang_key = "cpp"
    
    action = "reset" if "reset" in match.group(0).lower() else "put"
    cell = match.group(3).upper() if action == "put" else ""

    print(f"Detected Move -> Lang: {lang_name} ({lang_key}), Action: {action}, Cell: {cell}")

    # 1. Load Global State
    if not os.path.exists(STATE_FILE):
        print("State file not found!")
        sys.exit(1)

    with open(STATE_FILE, 'r') as f:
        state = json.load(f)

    if lang_key not in state:
        # Try to find closely matching key
        keys = state.keys()
        found = False
        for k in keys:
            if k in lang_key or lang_key in k:
                lang_key = k
                found = True
                break
        if not found:
            print(f"Language {lang_key} not found in state.")
            sys.exit(1)

    # 2. Create Sandbox for Implementation
    with open(SANDBOX_FILE, 'w') as f:
        json.dump(state[lang_key], f, indent=2)

    # 3. Run Language Implementation
    env = os.environ.copy()
    env['LANG_KEY'] = lang_key
    env['CELL'] = cell
    env['ACTION'] = action

    impl_runners = {
        'python':     ['python3', 'implementations/python/game.py'],
        'javascript': ['node',   'implementations/javascript/game.js'],
        'typescript': ['npx', 'ts-node', 'implementations/typescript/game.ts'],
        'go':         ['go', 'run', 'implementations/go/game.go'],
        'rust':       ['./implementations/rust/target/release/game'],
        'java':       ['java', '-cp', 'implementations/java', 'Game'],
        'kotlin':     ['java', '-jar', 'implementations/kotlin/Game.jar'],
        'php':        ['php',  'implementations/php/game.php'],
        'ruby':       ['ruby', 'implementations/ruby/game.rb'],
        'scala':      ['scala', '-cp', 'implementations/scala', 'Game'],
        'c':          ['./implementations/c/game'],
        'cpp':        ['./implementations/cpp/game'],
        'csharp':     ['dotnet', 'run', '--project', 'implementations/csharp', '--no-build'],
        'swift':      ['./implementations/swift/game'],
    }

    if lang_key not in impl_runners:
        print(f"No runner defined for {lang_key}")
        sys.exit(1)

    cmd = impl_runners[lang_key]
    print(f"Executing: {' '.join(cmd)}")
    result = subprocess.run(cmd, env=env)

    if result.returncode != 0:
        print("Implementation failed!")
        sys.exit(1)

    # 4. Load Sandbox back to Global State
    with open(SANDBOX_FILE, 'r') as f:
        state[lang_key] = json.load(f)

    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

    # 5. Update README
    update_readme(lang_name, lang_key, state[lang_key])

def update_readme(lang_name, lang_key, lang_state):
    with open("README.md", "r") as f:
        readme = f.read()

    # Generate Board Table
    new_board = render_board_table(lang_state['board'], lang_name)
    
    # Generate Turn/Winner status
    status = ""
    if lang_state['winner']:
        if lang_state['winner'] == 'draw':
            status = "🤝 **It's a draw!**"
        else:
            p = "❌" if lang_state['winner'] == 'X' else "⭕"
            status = f"🏆 **{p} {lang_state['winner']} wins!**"
    else:
        p = "❌" if lang_state['turn'] == 'X' else "⭕"
        status = f"Turn: {p} **{lang_state['turn']}** is next"

    # Reset Link
    reset_url = f"https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title={lang_name.replace('+', '%2B').replace('#', '%23')}%3A+Tic-Tac-Toe%3A+Reset&body=Reset+{lang_name}+board"
    reset_link = f"\n\n[🔄 Reset Board]({reset_url})"

    # Find the section tag
    tag = lang_key.upper().replace("CPP", "CPPLUS")
    # Fallback to name if key doesn't work for tags used in README
    if f"<!-- {tag}_START -->" not in readme:
        # Try finding by name if key is different
        tag = lang_name.upper().replace("C#", "CSHARP").replace("C++", "CPPLUS")

    pattern = f"<!-- {tag}_START -->.*?<!-- {tag}_END -->"
    replacement = f"<!-- {tag}_START -->\n{new_board}\n\n{status}{reset_link}\n<!-- {tag}_END -->"
    
    new_readme = re.sub(pattern, replacement, readme, flags=re.DOTALL)
    
    with open("README.md", "w") as f:
        f.write(new_readme)
    print("README updated successfully.")

if __name__ == "__main__":
    main()
