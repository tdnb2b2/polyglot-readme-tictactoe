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

def render_board_md(board: list, lang_key: str = "python", owner: str = "tdnb2b2", repo: str = "polyglot-readme-tictactoe",
                    turn: str = "X", winner: str = None, log: list = None,
                    input_info: str = "", output_info: str = "") -> str:
    """
    Renders the Tic-Tac-Toe board as a clean Markdown table with interactive links.
    Includes Next Move status, Recent moves, Technical Details, and New Game link when finished.
    """
    from urllib.parse import quote_plus
    
    # Compatibility: if called as render_board_md(board, logs)
    if log is None and (isinstance(lang_key, list) or lang_key is None):
        log = lang_key if isinstance(lang_key, list) else []
        lang_key = "python"

    if log is None:
        log = []

    # Normalize logs
    normalized = []
    for e in log:
        n = _normalize_log_entry(e)
        if n is not None:
            normalized.append(n)
    if not normalized and log:
        # Fallback if normalization fails but log exists
        # Handle string logs for SYMBOLS.get if they aren't dicts
        normalized = []
        for e in log:
            if isinstance(e, dict):
                normalized.append(e)
            else:
                normalized.append({"player": str(e), "cell": ""})

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
    rows = ['|   | A | B | C |   |', '|---|---|---|---|---|']
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
                # Properly URL-encode lang_display to handle + in C++ and C#
                safe_lang = quote_plus(lang_display)
                title = f"{safe_lang}%3A+Tic-Tac-Toe%3A+Put+{cell_name}"
                body = f"Play+{safe_lang}+board"
                link = f'https://github.com/{owner}/{repo}/issues/new?title={title}&body={body}'
                # Escape pipe character in URL to prevent breaking markdown table
                safe_link = link.replace('|', '%7C')
                cells.append(f'[___]({safe_link})')
        cells.append(f'**{row_label}**')
        rows.append(f'| {" | ".join(cells)} |')

    rows.append('|   | A | B | C |   |')
    # Ensure there's a blank line before the table for GitHub rendering
    board_md = '\n' + '\n'.join(rows)

    # Status
    if winner:
        if winner == 'draw':
            status = '🤝 **Game Draw**'
        else:
            status = f'🏆 **Winner: {SYMBOLS.get(winner, winner)} ({lang_display})**'
    else:
        status = f"🎮 **Next Move: {SYMBOLS.get(turn, turn)} ({lang_display})**"

    # Recent moves
    log_md = ""
    if normalized:
        recent = normalized[-5:]
        moves = []
        for m in recent:
            p = SYMBOLS.get(m.get('player'), m.get('player'))
            c = m.get('cell', '')
            if p == '___' and not c:
                moves.append("Draw")
            else:
                moves.append(f"{p} {c}".strip())
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

    return board_md + "\n\n" + status + log_md + new_game_link + "\n" + tech_details

