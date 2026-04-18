#!/usr/bin/env python3
"""shared/board.py — shared README update utilities used by all implementations."""
import os
import re
import json
import urllib.request


def load_state(lang_key: str) -> dict:
    with open('game_state.json', 'r') as f:
        all_states = json.load(f)
    return all_states[lang_key]


def save_state(lang_key: str, state: dict):
    with open('game_state.json', 'r') as f:
        all_states = json.load(f)
    all_states[lang_key] = state
    with open('game_state.json', 'w') as f:
        json.dump(all_states, f, indent=2)


def get_readme(token: str, repo: str) -> tuple:
    url = f'https://api.github.com/repos/{repo}/contents/README.md'
    req = urllib.request.Request(url, headers={
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    })
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"Error fetching README: {e}")
        raise
    import base64
    content = base64.b64decode(data['content']).decode('utf-8')
    return content, data['sha']


def update_readme_local(content: str):
    with open('README.md', 'w') as f:
        f.write(content)


def update_readme(token: str, repo: str, content: str, sha: str, actor: str, lang: str):
    import base64
    url = f'https://api.github.com/repos/{repo}/contents/README.md'
    payload = json.dumps({
        'message': f'game({lang}): move by @{actor}',
        'content': base64.b64encode(content.encode()).decode(),
        'sha': sha,
        'branch': 'main',
    }).encode()
    req = urllib.request.Request(url, data=payload, headers={
        'Authorization': f'token {token}',
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.github.v3+json',
    })
    req.get_method = lambda: 'PUT'
    urllib.request.urlopen(req)


def replace_section(content: str, tag: str, new_body: str) -> str:
    pattern = rf'<!-- {re.escape(tag)}_START -->.*?<!-- {re.escape(tag)}_END -->'
    replacement = f'<!-- {tag}_START -->\n{new_body}\n<!-- {tag}_END -->'
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def post_comment(token: str, repo: str, issue_number: str, body: str):
    url = f'https://api.github.com/repos/{repo}/issues/{issue_number}/comments'
    payload = json.dumps({'body': body}).encode()
    req = urllib.request.Request(url, data=payload, headers={
        'Authorization': f'token {token}',
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.github.v3+json',
    })
    urllib.request.urlopen(req)


def close_issue(token: str, repo: str, issue_number: str):
    url = f'https://api.github.com/repos/{repo}/issues/{issue_number}'
    payload = json.dumps({'state': 'closed'}).encode()
    req = urllib.request.Request(url, data=payload, headers={
        'Authorization': f'token {token}',
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.github.v3+json',
    })
    req.get_method = lambda: 'PATCH'
    urllib.request.urlopen(req)


CELL_TO_IDX = {
    'A1': (0,0), 'B1': (0,1), 'C1': (0,2),
    'A2': (1,0), 'B2': (1,1), 'C2': (1,2),
    'A3': (2,0), 'B3': (2,1), 'C3': (2,2),
}

WIN_LINES = [
    [(0,0),(0,1),(0,2)],
    [(1,0),(1,1),(1,2)],
    [(2,0),(2,1),(2,2)],
    [(0,0),(1,0),(2,0)],
    [(0,1),(1,1),(2,1)],
    [(0,2),(1,2),(2,2)],
    [(0,0),(1,1),(2,2)],
    [(0,2),(1,1),(2,0)],
]


def check_winner(board: list) -> str:
    for line in WIN_LINES:
        vals = [board[r][c] for r, c in line]
        if vals[0] and vals[0] == vals[1] == vals[2]:
            return vals[0]
    return None


def is_draw(board: list) -> bool:
    return all(board[r][c] for r in range(3) for c in range(3))


def render_board_md(board: list, lang_key: str, owner: str, repo: str,
                    turn: str, winner: str, log: list) -> str:
    # Minimalist status symbols
    SYMBOLS = {'X': '❌', 'O': '⭕', '': '___'}
    LANG_DISPLAY = {
        'python': 'Python', 'javascript': 'JavaScript', 'typescript': 'TypeScript',
        'go': 'Go', 'rust': 'Rust', 'java': 'Java', 'kotlin': 'Kotlin',
        'php': 'PHP', 'ruby': 'Ruby', 'csharp': 'C#', 'c': 'C',
        'cpp': 'C++', 'scala': 'Scala', 'swift': 'Swift',
    }
    lang_display = LANG_DISPLAY.get(lang_key, lang_key)
    
    rows = ['|   | A | B | C |   |', '|---|---|---|---|---|']
    for ri, row_label in enumerate(['1', '2', '3']):
        cells = [f'**{row_label}**']
        for ci in range(3):
            val = board[ri][ci]
            cell_name = f"{['A','B','C'][ci]}{ri+1}"
            
            if val:
                cells.append(SYMBOLS[val])
            elif winner:
                cells.append('___')
            else:
                title = f"{lang_display}%3A+Tic-Tac-Toe%3A+Put+{cell_name}"
                link = f'https://github.com/{owner}/{repo}/issues/new?title={title}&body=Play+{lang_display}+board'
                # Minimalist link text
                cells.append(f'[___]({link})')
        cells.append(f'**{row_label}**')
        rows.append(f'| {" | ".join(cells)} |')
    
    rows.append('|   | A | B | C |   |')
    board_md = '\n'.join(rows)

    if winner:
        reset_title = f"{lang_display}%3A+Tic-Tac-Toe%3A+Reset"
        status = f'{winner} wins! — [Reset](https://github.com/{owner}/{repo}/issues/new?title={reset_title}&body=Reset+the+board)'
    elif is_draw(board):
        reset_title = f"{lang_display}%3A+Tic-Tac-Toe%3A+Reset"
        status = f"It's a draw! — [Reset](https://github.com/{owner}/{repo}/issues/new?title={reset_title}&body=Reset+the+board)"
    else:
        status = f'Turn: {SYMBOLS[turn]} {turn} is next'

    log_md = ''
    if log:
        recent = log[-5:]
        log_md = '\n\nRecent moves: ' + ' -> '.join(
            f'{e["player"]} {e["cell"]}' for e in recent
        )

    return f'{board_md}\n\n{status}{log_md}\n'
