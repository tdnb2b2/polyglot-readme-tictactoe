import os
import json
import re

# Simple 3x3 Tic-Tac-Toe board state mapping
CELL_TO_IDX = {
    'A1': (0, 0), 'B1': (0, 1), 'C1': (0, 2),
    'A2': (1, 0), 'B2': (1, 1), 'C2': (1, 2),
    'A3': (2, 0), 'B3': (2, 1), 'C3': (2, 2)
}

def get_source_code(lang_key: str) -> str:
    """Retrieves source code for the specific language implementation."""
    lang_file_map = {
        'python': 'game.py',
        'javascript': 'game.js',
        'typescript': 'game.ts',
        'go': 'game.go',
        'rust': 'src/main.rs',
        'java': 'Game.java',
        'kotlin': 'Game.kt',
        'php': 'game.php',
        'ruby': 'game.rb',
        'csharp': 'Program.cs',
        'c': 'game.c',
        'cpp': 'game.cpp',
        'scala': 'Game.scala',
        'swift': 'game.swift'
    }
    
    filename = lang_file_map.get(lang_key)
    if not filename:
        return f"// Source code mapping for {lang_key} not defined."

    path = os.path.join('implementations', lang_key, filename)
    try:
        if os.path.exists(path):
            with open(path, 'r') as f:
                return f.read()
        return f"// Source code for {lang_key} not found at {path}"
    except Exception as e:
        return f"// Error reading source for {lang_key}: {str(e)}"

def update_readme_local(new_content: str):
    """Writes updated content to README.md in current directory."""
    with open('README.md', 'w') as f:
        f.write(new_content)

def replace_section(content: str, tag: str, replacement: str) -> str:
    """Replaces a section marked by <!-- BOARD_TAG_START --> and <!-- BOARD_TAG_END -->."""
    start_tag = f"<!-- {tag}_START -->"
    end_tag = f"<!-- {tag}_END -->"
    
    pattern = re.compile(rf"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.DOTALL)
    if not pattern.search(content):
        return content
        
    return pattern.sub(f"{start_tag}\n{replacement}\n{end_tag}", content)

def render_board_md(board: list, lang_key: str, owner: str, repo: str,
                    turn: str, winner: str, log: list,
                    input_info: str = "", output_info: str = "") -> str:
    """
    Renders the Tic-Tac-Toe board as a clean Markdown table with interactive links.
    Includes Next Move status, Recent moves, Technical Details, and New Game link when finished.
    """
    from urllib.parse import quote_plus
    
    # Minimalist status symbols
    SYMBOLS = {'X': '❌', 'O': '⭕', '': '___'}
    LANG_DISPLAY = {
        'python': 'Python', 'javascript': 'JavaScript', 'typescript': 'TypeScript',
        'go': 'Go', 'rust': 'Rust', 'java': 'Java', 'kotlin': 'Kotlin',
        'php': 'PHP', 'ruby': 'Ruby', 'csharp': 'C#', 'c': 'C',
        'cpp': 'C++', 'scala': 'Scala', 'swift': 'Swift',
    }
    lang_display = LANG_DISPLAY.get(lang_key, lang_key)

    # Board table
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
                # Escape pipe character in URL to prevent breaking markdown table
                safe_link = link.replace('|', '%7C')
                cells.append(f'[___]({safe_link})')
        cells.append(f'**{row_label}**')
        rows.append(f'| {" | ".join(cells)} |')

    rows.append('|   | A | B | C |   |')
    board_md = '\n'.join(rows)

    # Status
    if winner:
        if winner == 'draw':
            status = '🤝 Game Draw'
        else:
            status = f'🏆 Winner: {SYMBOLS.get(winner, winner)} ({lang_display})'
    else:
        status = f"🎮 **Next Move: {SYMBOLS.get(turn, turn)} ({lang_display})**"

    # Recent moves
    log_md = ""
    if log and len(log) > 0:
        recent = log[-5:]
        moves = [f"{SYMBOLS.get(m['player'], m['player'])} {m['cell']}" for m in recent]
        log_md = f"\n\nRecent moves: {' → '.join(moves)}"

    # New Game link (only when game is finished)
    new_game_link = ""
    if winner:
        reset_title = quote_plus(f"{lang_display}: Tic-Tac-Toe: Reset")
        reset_body = quote_plus(f"Start a new {lang_display} game")
        reset_url = f"https://github.com/{owner}/{repo}/issues/new?title={reset_title}&body={reset_body}"
        new_game_link = f"\n\n🔵 **[Start New Game]({reset_url})**"

    # Technical Details
    code_content = get_source_code(lang_key)
    code_ext = {'python': 'python', 'javascript': 'javascript', 'typescript': 'typescript',
                'go': 'go', 'rust': 'rust', 'java': 'java', 'kotlin': 'kotlin',
                'php': 'php', 'ruby': 'ruby', 'csharp': 'csharp', 'c': 'c',
                'cpp': 'cpp', 'scala': 'scala', 'swift': 'swift'}.get(lang_key, '')

    tech_details = f"""

<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `{input_info}`
- **Output (Information given)**:
```text
{output_info if output_info else "Success"}
```

### 💻 Implementation Code ({lang_display})
```{code_ext}
{code_content}
```
</details>
"""

    return board_md + "\n\n" + status + log_md + new_game_link + tech_details
