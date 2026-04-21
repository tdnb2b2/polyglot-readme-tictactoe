import os
import re
from urllib.parse import quote_plus

CELL_TO_IDX = {
    'A1': (0, 0), 'B1': (0, 1), 'C1': (0, 2),
    'A2': (1, 0), 'B2': (1, 1), 'C2': (1, 2),
    'A3': (2, 0), 'B3': (2, 1), 'C3': (2, 2)
}

LANG_DISPLAY = {
    'python': 'Python', 'javascript': 'JavaScript', 'typescript': 'TypeScript',
    'go': 'Go', 'rust': 'Rust', 'java': 'Java', 'kotlin': 'Kotlin',
    'php': 'PHP', 'ruby': 'Ruby', 'csharp': 'C#', 'c': 'C',
    'cpp': 'C++', 'scala': 'Scala', 'swift': 'Swift',
}

def get_source_code(lang_key: str) -> str:
    lang_file_map = {
        'python': 'game.py', 'javascript': 'game.js', 'typescript': 'game.ts',
        'go': 'game.go', 'rust': 'src/main.rs', 'java': 'Game.java',
        'kotlin': 'Game.kt', 'php': 'game.php', 'ruby': 'game.rb',
        'csharp': 'Program.cs', 'c': 'game.c', 'cpp': 'game.cpp',
        'scala': 'Game.scala', 'swift': 'game.swift'
    }
    filename = lang_file_map.get(lang_key)
    if not filename:
        return f"// Source code mapping for {lang_key} not defined."
    path = os.path.join('implementations', lang_key, filename)
    try:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
                content = content.replace('\x00', '')
                content = content.replace('```', '` ` `')
                return content
        return f"// Source code for {lang_key} not found at {path}"
    except Exception as e:
        return f"// Error reading source for {lang_key}: {str(e)}"

def replace_section(content: str, tag: str, replacement: str) -> str:
    start_tag = f"<!-- {tag}_START -->"
    end_tag = f"<!-- {tag}_END -->"
    pattern = re.compile(rf"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.DOTALL)
    if not pattern.search(content):
        return content
    return pattern.sub(lambda _: f"{start_tag}\n{replacement}\n{end_tag}", content)

def render_board_md(board: list, lang_key: str, owner: str, repo: str,
                    turn: str = "", winner: str = "", log: list = None,
                    input_info: str = "", output_info: str = "") -> str:
    """
    Renders the Tic-Tac-Toe board as a clean Markdown table with interactive links.
    Returns only the board table - no status, log, or technical details.
    """
    lang_display = LANG_DISPLAY.get(lang_key, lang_key.capitalize())
    SYMBOLS = {'X': '❌', 'O': '⭕', '': '___'}

    rows = ['|   | A | B | C |   |', '|---|---|---|---|---|']
    for ri in range(3):
        row_label = str(ri + 1)
        cells = [f'**{row_label}**']
        for ci in range(3):
            val = board[ri][ci]
            cell_name = f"{['A', 'B', 'C'][ci]}{ri + 1}"
            if val:
                cells.append(SYMBOLS.get(val, val))
            elif winner:
                cells.append('___')
            else:
                title_str = f"{lang_display}: Tic-Tac-Toe: Put {cell_name}"
                body_str = f"Play {lang_display} board"
                link = f'https://github.com/{owner}/{repo}/issues/new?title={quote_plus(title_str)}&body={quote_plus(body_str)}'
                cells.append(f'[___]({link})')
        cells.append(f'**{row_label}**')
        rows.append(f'| {" | ".join(cells)} |')

    rows.append('|   | A | B | C |   |')
    return '\n'.join(rows)
