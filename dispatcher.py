import os
import sys
import json
import subprocess
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
ISSUE_TITLE = os.getenv("ISSUE_TITLE", "")
ISSUE_NUMBER = os.getenv("ISSUE_NUMBER")
REPO = os.getenv("REPO")

LANGUAGES = {
    "python": {"cmd": ["python3", "implementations/python/game.py"]},
    "javascript": {"cmd": ["node", "implementations/javascript/game.js"]},
    "typescript": {"cmd": ["ts-node", "implementations/typescript/game.ts"]},
    "go": {"cmd": ["go", "run", "implementations/go/game.go"]},
    "rust": {"cmd": ["./implementations/rust/target/release/game"]},
    "ruby": {"cmd": ["ruby", "implementations/ruby/game.rb"]},
    "php": {"cmd": ["php", "implementations/php/game.php"]},
    "java": {"cmd": ["java", "implementations/java/Game"]},
    "cpp": {"cmd": ["./implementations/cpp/game"]},
    "c": {"cmd": ["./implementations/c/game"]},
    "csharp": {"cmd": ["dotnet", "run", "--project", "implementations/csharp/game.csproj"]},
    "swift": {"cmd": ["swift", "implementations/swift/game.swift"]},
    "kotlin": {"cmd": ["kotlin", "implementations/kotlin/game.jar"]},
    "scala": {"cmd": ["scala", "implementations/scala/game.scala"]}
}

def detect_language():
    # Allow override from env (set by specific workflow)
    override = os.getenv("LANGUAGE_OVERRIDE")
    if override and override in LANGUAGES:
        return override

    title = ISSUE_TITLE.lower()
    for lang in LANGUAGES:
        if lang in title:
            return lang
    return None

def parse_move(title):
    import re
    match = re.search(r"put\s+([a-c][1-3])", title.lower())
    if match:
        return match.group(1).upper()
    return None

def update_readme(board_md):
    with open("README.md", "r") as f:
        content = f.read()
    
    import re
    # Look for the board section
    new_content = re.sub(
        r"<!-- BOARD_START -->.*?<!-- BOARD_END -->",
        f"<!-- BOARD_START -->\n{board_md}\n<!-- BOARD_END -->",
        content,
        flags=re.DOTALL
    )
    
    with open("README.md", "w") as f:
        f.write(new_content)

def run():
    lang_key = detect_language()
    if not lang_key:
        print(f"Language not detected from title: {ISSUE_TITLE}")
        return

    move = parse_move(ISSUE_TITLE)
    if not move:
        print(f"Move not detected from title: {ISSUE_TITLE}")
        return

    # Call language implementation
    cmd = LANGUAGES[lang_key]["cmd"] + [move]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error running {lang_key}: {result.stderr}")
        return

    # Implementation should update game_state.json
    # Now we re-render the board using shared/board.py logic (via python)
    from shared.board import render_board_md
    with open("game_state.json", "r") as f:
        state = json.load(f)
    
    board_md = render_board_md(state["board"])
    update_readme(board_md)
    
    # Close issue
    if GITHUB_TOKEN and REPO and ISSUE_NUMBER:
        url = f"https://api.github.com/repos/{REPO}/issues/{ISSUE_NUMBER}/comments"
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        requests.post(url, json={"body": f"Move {move} processed by {lang_key.capitalize()} workflow."}, headers=headers)
        
        url_close = f"https://api.github.com/repos/{REPO}/issues/{ISSUE_NUMBER}"
        requests.patch(url_close, json={"state": "closed"}, headers=headers)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        run()
