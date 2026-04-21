import os
import json
import re

# Simple 3x3 Tic-Tac-Toe board state mapping
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
            with open(path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
                content = content.replace('\x00', '')
                content = content.replace('```', '` ` `')
                return content
        return f"// Source code for {lang_key} not found at {path}"
    except Exception as e:
        return f"// Error reading source for {lang_key}: {str(e)}"

def replace_section(content: str, tag: str, replacement: str) -> str:
    """Replaces a section marked by <!-- BOARD_TAG_START --> and <!-- BOARD_TAG_END -->."""
    start_tag = f"<!-- {tag}_START -->"
    end_tag = f"<!-- {tag}_END -->"
    pattern = re.compile(rf"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.DOTALL)
    if not pattern.search(content):
        return content
    # Use lambda to prevent backslash interpretation (binary corruption fix)
    return pattern.sub(lambda _: f"{start_tag}\n{replacement}\n{end_tag}", content)

def render_board_md(board: list, lang_key: str, owner: str, repo: str,
                    turn: str, winner: str, log: list, 
                    input_info: str = "", output_info: str = "") -> str:
    """
    Renders the Tic-Tac-Toe board as a Markdown table with interactive links.
    Includes technical details (source code and execution context).
    """
    lang_display = LANG_DISPLAY.get(lang_key, lang_key.capitalize())
    
    if winner:
        if winner == 'draw':
            status = "🤝 **It's a Draw!**"
        else:
            status = f"🏆 **Winner: {winner} ({lang_display})**"
    else:
        status = f"🎮 **Next Move: {turn} ({lang_display})**"

    # Minimalist status symbols
    SYMBOLS = {'X': '❌', 'O': '⭕', '': '___'}
    
    rows = ['|   | A | B | C |   |', '|---|---|---|---|---|']
    for ri, row_label in enumerate(['1', '2', '3']):
        cells = [f'**{row_label}**']
        for ci in range(3):
            val = board[ri][ci]
            cell_name = f"{['A','B','C'][ci]}{ri+1}"
            
            if val:
                cells.append(SYMBOLS.get(val, val))
            elif winner:
                cells.append('___')
            else:
                title = f"{lang_display}%3A+Tic-Tac-Toe%3A+Put+{cell_name}"
                link = f'https://github.com/{owner}/{repo}/issues/new?title={title}&body=Play+{lang_display}+board'
                cells.append(f'[___]({link})')
        cells.append(f'**{row_label}**')
        rows.append(f'| {" | ".join(cells)} |')
    
    rows.append('|   | A | B | C |   |')
    board_md = '\n'.join(rows)

    log_md = ''
    if log:
        recent = log[-5:]
        log_md = '\n\nRecent moves: ' + ' → '.join(
            f'{e["player"]} {e["cell"]}' for e in recent
        )

    # Technical Details (Collapsible)
    code_content = get_source_code(lang_key)
    code_ext = 'cs' if lang_key == 'csharp' else lang_key

    tech_details = f"""
<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `{input_info or "Initial Page Load / Manual Sync"}`
- **Output (Information given)**: 
```text
{output_info or "Move processed successfully."}
```

### 💻 Implementation Code ({lang_display})
```{code_ext}
{code_content}
```
</details>
"""

    return f'{board_md}\n\n{status}{log_md}\n{tech_details}'
