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
        token   = os.environ['GITHUB_TOKEN']
        repo    = os.environ['REPO']
        issue_n = os.environ['ISSUE_NUMBER']
        _close_issue(token, repo, issue_n,
            f'Unknown command: `{title}`\n\n'
            'Expected format: `<Language>: Tic-Tac-Toe: Put <A-C><1-3>`\n\n'
            'Supported languages: Python, JavaScript, TypeScript, Go, Rust, '
            'Java, Kotlin, PHP, Ruby, C#, C++, Scala, Swift, C')
        sys.exit(0)

    # Dispatch to language implementation via subprocess
    env = dict(os.environ)
    env['LANG_KEY'] = lang
    env['CELL']     = cell or ''
    env['ACTION']   = action

    impl_runners = {
        'python':     ['python', 'implementations/python/game.py'],
        'javascript': ['node',   'implementations/javascript/game.js'],
        'typescript': ['npx', 'ts-node', 'implementations/typescript/game.ts'],
        'go':         ['go', 'run', 'implementations/go/game.go'],
        'rust':       ['./implementations/rust/target/release/game'],
        'java':       ['java', '-cp', 'implementations/java', 'Game'],
        'kotlin':     ['kotlin', 'implementations/kotlin/GameKt'],
        'php':        ['php',    'implementations/php/game.php'],
        'ruby':       ['ruby',   'implementations/ruby/game.rb'],
        'csharp':     ['dotnet', 'run', '--project', 'implementations/csharp'],
        'c':          ['./implementations/c/game'],
        'cpp':        ['./implementations/cpp/game'],
        'scala':      ['scala',  'implementations/scala/Game.scala'],
        'swift':      ['swift',  'implementations/swift/game.swift'],
    }

    cmd = impl_runners[lang]
    result = subprocess.run(cmd, env=env, capture_output=False)
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
    req = urllib.request.Request(f'{base}/comments', data=data, headers=headers)
    urllib.request.urlopen(req)
    data2 = json.dumps({'state': 'closed'}).encode()
    req2 = urllib.request.Request(base, data=data2, headers=headers,
                                   method='PATCH')
    urllib.request.urlopen(req2)


if __name__ == '__main__':
    main()
