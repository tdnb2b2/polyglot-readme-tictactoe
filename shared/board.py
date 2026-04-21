import os
import json
import re
from urllib.parse import quote_plus

# Constants
SYMBOLS = {'X': '❌', 'O': '⭕', '': '___'}
CONFIG = {
    'c': {'name': 'C'},
    'cpp': {'name': 'C++'},
    'csharp': {'name': 'C#'},
    'go': {'name': 'Go'},
    'java': {'name': 'Java'},
    'javascript': {'name': 'JavaScript'},
    'kotlin': {'name': 'Kotlin'},
    'php': {'name': 'PHP'},
    'python': {'name': 'Python'},
    'ruby': {'name': 'Ruby'},
    'rust': {'name': 'Rust'},
    'scala': {'name': 'Scala'},
    'swift': {'name': 'Swift'},
    'typescript': {'name': 'TypeScript'},
}

def clean_source_code(code):
    """
    Sanitizes source code for embedding in Markdown.
    1. Replaces null bytes with escaped sequence to prevent binary corruption.
    2. Escapes triple backticks to prevent Markdown breaking.
    """
    if not code:
        return ""
    # Explicitly handle null bytes which cause 'data' file type detection in git
    # We use double backslash to ensure it stays as \0 in the text
    code = code.replace('\x00', '\\\\0')
    # Escape triple backticks by adding zero-width space or similar, 
    # but here we'll just do the space trick which is safer for most viewers
    code = code.replace('```', '`\\`\\`')
    return code

def get_source_code(lang_key):
    """Retrieves source code for the specific language implementation."""
    lang_file_map = {
        'python': 'game.py',
        'javascript': 'game.js',
        'typescript': 'game.ts',
        'go': 'game.go',
        'rust': 'src/main.rs',
        'java': 'Game.java',
        'kotlin': 'game.kt',
        'php': 'game.php',
        'ruby': 'game.rb',
        'csharp': 'Program.cs',
        'c': 'game.c',
        'cpp': 'game.cpp',
        'scala': 'game.scala',
        'swift': 'game.swift'
    }
    
    filename = lang_file_map.get(lang_key)
    if not filename:
        return f"// Source code mapping for {lang_key} not defined."

    path = os.path.join('implementations', lang_key, filename)
    try:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            return clean_source_code(content)
        return f"// Source code for {lang_key} not found at {path}"
    except Exception as e:
        return f"// Error reading source for {lang_key}: {str(e)}"

def replace_section(content, name, new_section):
    """
    Replaces a section in content marked by <!-- NAME_START --> and <!-- NAME_END -->
    Uses a lambda for replacement to avoid any backslash interpolation issues.
    """
    pattern = rf"(<!-- {name}_START -->).*?(<!-- {name}_END -->)"
    # Using lambda m: ... to prevent re.sub from interpreting backslashes in new_section
    try:
        return re.sub(pattern, lambda m: f"{m.group(1)}\n{new_section}\n{m.group(2)}", content, flags=re.DOTALL)
    except Exception as e:
        print(f"Error in replace_section for {name}: {e}")
        return content

def render_board_md(lang_key, state, owner="tdnb2b2", repo="polyglot-readme-tictactoe"):
    """
    Renders the Tic-Tac-Toe board as a Markdown table with interactive links.
    """
    board = state.get('board', [['']*3 for _ in range(3)])
    turn = state.get('turn', 'X')
    winner = state.get('winner')
    
    # Use standard 4-column layout
    board_md = "| | A | B | C |\n|---|---|---|---|\n"
    for i in range(3):
        row_str = f"| {i+1} | "
        for j in range(3):
            cell_val = board[i][j]
            symbol = SYMBOLS.get(cell_val, '___')
            
            # Create link for move
            cell_id = f"{chr(65+j)}{i+1}"
            lang_name = CONFIG.get(lang_key, {}).get('name', lang_key.upper())
            title = f"{lang_name}: Tic-Tac-Toe: Put {cell_id}"
            body = f"Play {lang_name} board"
            url = f"https://github.com/{owner}/{repo}/issues/new?title={quote_plus(title)}&body={quote_plus(body)}"
            
            row_str += f"[{symbol}]({url}) | "
        board_md += row_str + "\n"
    
    lang_display = CONFIG.get(lang_key, {}).get('name', lang_key.upper())
    
    # Status line
    if winner:
        if winner == 'draw':
            status = f"🏁 **Result: Draw! ({lang_display})**"
        else:
            status = f"🏆 **Winner: {winner} ({lang_display})**"
        
        # Add reset link if game over
        reset_title = f"{lang_display}: Tic-Tac-Toe: Reset"
        reset_url = f"https://github.com/{owner}/{repo}/issues/new?title={quote_plus(reset_title)}&body=Reset+the+board"
        status += f" [🔄 Reset]({reset_url})"
    else:
        status = f"🎮 **Next Move: {turn} ({lang_display})**"
            
    log_md = ""
    if state.get('log'):
        log_md = "\n\n### 📝 Move History\n"
        # Only show last 10 moves to keep it concise
        moves = state['log'][-10:]
        if len(state['log']) > 10:
            log_md += "... (older moves hidden) ...\n"
        for i, move in enumerate(moves):
            log_md += f"{i+1}. {move['player']} at {move['cell']}\n"
            
    # Technical Details
    tech_details = f"\n<details>\n<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>\n\n"
    
    # Execution Context
    tech_details += f"### 🛰️ Execution Context\n```json\n{json.dumps(state, indent=2)}\n```\n\n"
    
    # Implementation Code
    tech_details += f"### 💻 Implementation Code ({lang_display})\n"
    tech_details += f"``` {lang_key}\n"
    code_content = get_source_code(lang_key)
    tech_details += f"{code_content}\n"
    tech_details += "```\n"
    tech_details += "</details>"
    
    return f"{board_md}\n\n{status}{log_md}\n{tech_details}"
