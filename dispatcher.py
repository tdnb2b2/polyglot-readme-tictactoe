#!/usr/bin/env python3
"""dispatcher.py — detects language from issue title and routes to implementation."""
import os
import re
import sys
import json
import subprocess

LANGUAGE_MAP = {
    "python":     "python",
    "javascript": "javascript",
    "typescript": "typescript",
    "go":         "go",
    "rust":       "rust",
    "java":       "java",
    "kotlin":     "kotlin",
    "php":        "php",
    "ruby":       "ruby",
    "c#":         "csharp",
    "csharp":     "csharp",
    "c++":        "cpp",
    "cpp":        "cpp",
    "scala":      "scala",
    "swift":      "swift",
    "c":          "c",
}

# Pattern: "<Language>: Tic-Tac-Toe: Put <Cell>"
TITLE_PAT = re.compile(
    r'^(?P<lang>[\w#+]+):\s*Tic-Tac-Toe:\s*Put\s+(?P<cell>[A-Ca-c][1-3])\s*$',
    re.IGNORECASE
)
RESET_PAT = re.compile(
    r'^(?P<lang>[\w#+]+):\s*Tic-Tac-Toe:\s*Reset\s*$',
    re.IGNORECASE
)


def detect_language(title: str):
    # Allow explicit override from CI
    override = os.environ.get('LANGUAGE_OVERRIDE')
    if override and override.lower() in LANGUAGE_MAP.values():
        lang = override.lower()
        # Still need cell if it's a put action
        m = TITLE_PAT.match(title)
        cell = m.groupdict().get('cell', '').upper() if m and 'cell' in m.groupdict() else None
        action = 'reset' if RESET_PAT.match(title) else 'put'
        return lang, cell, action

    m = TITLE_PAT.match(title) or RESET_PAT.match(title)
    if not m:
        return None, None, None
    raw_lang = m.group('lang').lower()
    lang = LANGUAGE_MAP.get(raw_lang)
    if not lang:
        return None, None, None
    cell = m.groupdict().get('cell', '').upper() if 'cell' in m.groupdict() else None
    action = 'reset' if RESET_PAT.match(title) else 'put'
    return lang, cell, action


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'run'
    title = os.environ.get('ISSUE_TITLE', '').strip()

    if mode == 'detect':
        lang, _, _ = detect_language(title)
        print(lang or 'unknown')
        return

    lang, cell, action = detect_language(title)

    if lang is None:
        token   = os.environ.get('GITHUB_TOKEN')
        repo    = os.environ.get('REPO')
        issue_n = os.environ.get('ISSUE_NUMBER')
        if token and repo and issue_n:
            _close_issue(token, repo, issue_n,
                f'Unknown command: {title}\n\n'
                'Expected format: <Language>: Tic-Tac-Toe: Put <A-C><1-3>\n\n'
                'Supported languages: Python, JavaScript, TypeScript, Go, Rust, '
                'Java, Kotlin, PHP, Ruby, C#, C++, Scala, Swift, C')
        else:
            print(f"Unknown command: {title}")
        sys.exit(0)

    # Prepare sandbox state
    with open('game_state.json', 'r', encoding='utf-8') as f:
        all_states = json.load(f)
    
    current_state = all_states.get(lang, {
        'board': [['','',''],['','',''],['','','']],
        'turn': 'X',
        'winner': None,
        'log': []
    })
    
    with open('current_state.json', 'w', encoding='utf-8') as f:
        json.dump(current_state, f)

    env = dict(os.environ)
    env['LANG_KEY'] = lang
    env['CELL']     = cell or ''
    env['ACTION']   = action

    # Determine implementation directory and simplified command
    impl_runners = {
        'python':     (['python3', 'game.py'], 'implementations/python'),
        'javascript': (['node',    'game.js'], 'implementations/javascript'),
        'typescript': (['npm', 'run', 'play'], 'implementations/typescript'),
        'go':         (['go', 'run', 'game.go'], 'implementations/go'),
        'rust':       (['cargo', 'run', '--release'], 'implementations/rust'),
        'java':       (['java', 'Game'], 'implementations/java'),
        'kotlin':     (['java', '-jar', 'Game.jar'], 'implementations/kotlin'),
        'php':        (['php',     'game.php'], 'implementations/php'),
        'ruby':       (['ruby',    'game.rb'], 'implementations/ruby'),
        'csharp':     (['dotnet', 'run', '--no-build'], 'implementations/csharp'),
        'c':          (['./game'], 'implementations/c'),
        'cpp':        (['./game'], 'implementations/cpp'),
        'scala':      (['scala',   'Game.scala'], 'implementations/scala'),
        'swift':      (['swift',   'game.swift'], 'implementations/swift'),
    }

    if lang not in impl_runners:
        print(f"Error: No runner defined for {lang}", file=sys.stderr)
        sys.exit(1)

    cmd, impl_dir = impl_runners[lang]
    state_path = os.path.join(impl_dir, 'current_state.json')

    # Prepare sandbox state in the implementation directory
    with open(state_path, 'w', encoding='utf-8') as f:
        json.dump(current_state, f)

    env = dict(os.environ)
    env['LANG_KEY'] = lang
    env['CELL']     = cell or ''
    env['ACTION']   = action

    print(f"Running {lang} implementation in {impl_dir}...")
    result = subprocess.run(cmd, env=env, cwd=impl_dir, capture_output=True, text=True)
    
    if result.returncode == 0:
        # Read back sandbox state from implementation directory
        with open(state_path, 'r', encoding='utf-8') as f:
            updated_state = json.load(f)
        
        all_states[lang] = updated_state
        with open('game_state.json', 'w', encoding='utf-8') as f:
            json.dump(all_states, f, indent=2)

        # Update README.md
        try:
            from shared.board import replace_section, render_board_md
            
            repo_full = os.environ.get('REPO', 'tdnb2b2/polyglot-readme-tictactoe')
            owner, repo = repo_full.split('/') if '/' in repo_full else ('tdnb2b2', 'polyglot-readme-tictactoe')

            with open('README.md', 'r', encoding='utf-8') as f:
                current_content = f.read()

            new_content = current_content

            # 1. Update all individual language boards to keep them in sync and clean up legacy corruption
            for l_key, l_state in all_states.items():
                l_md = render_board_md(
                    board=l_state['board'],
                    lang_key=l_key,
                    owner=owner,
                    repo=repo,
                    turn=l_state['turn'],
                    winner=l_state['winner'],
                    log=l_state['log']
                )
                new_content = replace_section(new_content, f"BOARD_{l_key.upper()}", l_md)

            if new_content != current_content:
                with open('README.md', 'w', encoding='utf-8') as f:
                    f.write(new_content)
            
            token      = os.environ.get('GITHUB_TOKEN')
            issue_n    = os.environ.get('ISSUE_NUMBER')
            
            if token and repo_full and issue_n:
                _close_issue(token, repo_full, issue_n, f"Move accepted for {lang}. README updated.")
            else:
                print(f"Move accepted for {lang}. README updated locally.")

        except Exception as e:
            print(f"Error updating README: {e}", file=sys.stderr)
    else:
        # On failure, dump stdout and stderr to help debug in CI
        print(f"Error: Command for {lang} failed with exit code {result.returncode}", file=sys.stderr)
        if result.stdout:
            print("--- STDOUT ---", file=sys.stderr)
            print(result.stdout, file=sys.stderr)
        if result.stderr:
            print("--- STDERR ---", file=sys.stderr)
            print(result.stderr, file=sys.stderr)

    if os.path.exists(state_path):
        os.remove(state_path)

    sys.exit(result.returncode)


def _close_issue(token, repo, issue_number, comment_body):
    import urllib.request
    headers = {
        'Authorization': f'token {token}',
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.github.v3+json',
    }
    base = f'https://api.github.com/repos/{repo}/issues/{issue_number}'
    data = json.dumps({'body': comment_body}).encode()

    req = urllib.request.Request(base + '/comments', data=data, headers=headers)
    with urllib.request.urlopen(req) as resp:
        pass

    data = json.dumps({'state': 'closed'}).encode()
    req = urllib.request.Request(base, data=data, headers=headers, method='PATCH')
    with urllib.request.urlopen(req) as resp:
        pass


if __name__ == '__main__':
    main()
