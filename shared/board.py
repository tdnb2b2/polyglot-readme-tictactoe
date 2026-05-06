import os
import json
import re
from urllib.parse import quote_plus

# Simple 3x3 Tic-Tac-Toe board state mapping
CELL_TO_IDX = {
    'A1': (0, 0), 'B1': (0, 1), 'C1': (0, 2),
    'A2': (1, 0), 'B2': (1, 1), 'C2': (1, 2),
    'A3': (2, 0), 'B3': (2, 1), 'C3': (2, 2)
}

def get_source_code(lang_key: str) -> str:
    """Retrieves source code for the specific language implementation."""
    # Mapping to actual entry files found in implementations/
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

def _normalize_log_entry(entry):
    if isinstance(entry, dict):
        if "player" in entry and "cell" in entry:
            return {"player": entry["player"], "cell": entry["cell"]}
        return None
    if isinstance(entry, str):
        s = entry.strip()
        if s.lower() == "draw":
            return {"player": None, "cell": None}
        if "->" in s:
            parts = [part.strip() for part in s.split("->", 1)]
            if len(parts) == 2:
                return {"player": parts[0], "cell": parts[1]}
    return None

def replace_section(content: str, tag: str, replacement: str) -> str:
    """Replaces a section marked by <!-- BOARD_TAG_START --> and <!-- BOARD_TAG_END -->."""
    start_tag = f"<!-- {tag}_START -->"
    end_tag = f"<!-- {tag}_END -->"
    
    pattern = re.compile(rf"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.DOTALL)
    if not pattern.search(content):
        return content
        
    return pattern.sub(f"{start_tag}\n{replacement}\n{end_tag}", content)

def render_board_md(board: list, lang_key: str = "python", owner: str = "tdnb2b2", repo: str = "polyglot-readme-tictactoe",
                    turn: str = "X", winner: str = None, log: list = None,
                    input_info: str = "", output_info: str = "") -> str:
    """
    Renders the Tic-Tac-Toe board as a clean Markdown table with interactive links.
    Includes Next Move status, Recent moves, Technical Details, and New Game link.
    """
    if log is None:
        log = []

    # Normalize logs
    normalized = []
    for e in log:
        n = _normalize_log_entry(e)
        if n is not None:
            normalized.append(n)
    
    # Minimalist status symbols
    SYMBOLS = {'X': '❌', 'O': '⭕', '': '___', None: '___'}
    LANG_DISPLAY = {
        'python': 'Python', 'javascript': 'JavaScript', 'typescript': 'TypeScript',
        'go': 'Go', 'rust': 'Rust', 'java': 'Java', 'kotlin': 'Kotlin',
        'php': 'PHP', 'ruby': 'Ruby', 'csharp': 'C#', 'c': 'C',
        'cpp': 'C++', 'scala': 'Scala', 'swift': 'Swift',
    }
    lang_display = LANG_DISPLAY.get(lang_key, lang_key)

    # Board table
    rows = ['| | A | B | C |', '|---|---|---|---|']
    for ri, row_label in enumerate(['1', '2', '3']):
        cells = [f'**{row_label}**']
        for ci in range(3):
            val = board[ri][ci] if ri < len(board) and ci < len(board[ri]) else None
            cell_name = f"{['A','B','C'][ci]}{ri+1}"

            if val:
                cells.append(SYMBOLS.get(val, val))
            elif winner:
                cells.append('___')
            else:
                safe_lang = quote_plus(lang_display)
                title = f"{safe_lang}%3A+Tic-Tac-Toe%3A+Put+{cell_name}"
                body = f"Play+{safe_lang}+board"
                link = f'https://github.com/{owner}/{repo}/issues/new?title={title}&body={body}'
                safe_link = link.replace('|', '%7C')
                cells.append(f'[___]({safe_link})')
        rows.append(f'| {" | ".join(cells)} |')

    board_md = '\n' + '\n'.join(rows) + '\n'

    # Status line
    if winner:
        if winner.lower() == 'draw':
            status = f"\n🤝 **Result: Draw!**\n"
        else:
            status = f"\n🏆 **Winner: {SYMBOLS.get(winner, winner)} ({lang_display})**\n"
    else:
        status = f"\n🎮 **Next Move: {SYMBOLS.get(turn, turn)} ({lang_display})**\n"

    # Log line (last 5 moves)
    log_md = ""
    if normalized:
        recent = normalized[-5:]
        moves_str = " → ".join([f"{SYMBOLS.get(m['player'], m['player'])} {m['cell']}" for m in recent])
        log_md = f"\nRecent moves: {moves_str}\n"

    # New Game link (always visible as requested)
    safe_lang = quote_plus(lang_display)
    new_game_link = f'\n🔵 **[Start New Game](https://github.com/{owner}/{repo}/issues/new?title={safe_lang}%3A+Tic-Tac-Toe%3A+Reset&body=Start+a+new+{safe_lang}+game)**\n'

    # Technical Details
    source_code = get_source_code(lang_key)
    # Highlight language key for syntax highlighting if possible
    syntax_lang = lang_key
    if lang_key == 'csharp': syntax_lang = 'csharp'
    if lang_key == 'cpp': syntax_lang = 'cpp'
    
    tech_details = f"""
<details>
<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>

### 🛰️ Execution Context
- **Input (Information received)**: `{input_info or "None"}`
- **Output (Information given)**:
```text
{output_info or "None"}
```

### 💻 Implementation Code ({lang_display})
```{syntax_lang}
{source_code}
```

</details>
"""
    return board_md + status + log_md + new_game_link + tech_details
