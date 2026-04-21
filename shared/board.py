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

def get_source_code(lang_key):
    \"\"\"Retrieves source code for the specific language implementation.\"\"\"
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
        return f\"// Source code mapping for {lang_key} not defined.\"

    path = os.path.join('implementations', lang_key, filename)
    try:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Sanitize: remove null bytes and other control characters that might break markdown
                content = content.replace('\x00', '\\\\0')
                # Escape triple backticks to avoid breaking markdown code blocks
                content = content.replace('```', '` ` `')
                return content
        return f\"// Source code for {lang_key} not found at {path}\"
    except Exception as e:
        return f\"// Error reading source for {lang_key}: {str(e)}\"

def replace_section(content, name, new_section):
    \"\"\"Replaces a section marked by <!-- NAME_START --> and <!-- NAME_END -->.\"\"\"
    pattern = f\"<!-- {name}_START -->.*?<!-- {name}_END -->\"
    replacement_text = f\"<!-- {name}_START -->\\n{new_section}\\n<!-- {name}_END -->\"
    
    if not re.search(pattern, content, re.DOTALL):
        print(f\"Warning: Section {name} not found in content\")
        return content
        
    # Use a lambda to avoid backslash interpolation in re.sub
    return re.sub(pattern, lambda _: replacement_text, content, flags=re.DOTALL)

def render_board_md(lang_key, state, owner=\"tdnb2b2\", repo=\"polyglot-readme-tictactoe\"):
    \"\"\"
    Renders the Tic-Tac-Toe board as a Markdown table with interactive links.
    \"\"\"
    board = state.get('board', [['']*3 for _ in range(3)])
    turn = state.get('turn', 'X')
    winner = state.get('winner')
    
    # Use standard 4-column layout
    board_md = \"| | A | B | C |\\n|---|---|---|---|\\n\"
    for i in range(3):
        row_str = f\"| {i+1} | \"
        for j in range(3):
            cell_val = board[i][j]
            symbol = SYMBOLS.get(cell_val, '___')
            
            # Create link for move
            cell_id = f\"{chr(65+j)}{i+1}\"
            lang_name = CONFIG.get(lang_key, {}).get('name', lang_key.upper())
            title = f\"{lang_name}: Tic-Tac-Toe: Put {cell_id}\"
            body = f\"Play {lang_name} board\"
            url = f\"https://github.com/{owner}/{repo}/issues/new?title={quote_plus(title)}&body={quote_plus(body)}\"
            
            row_str += f\"[{symbol}]({url}) | \"
        board_md += row_str + \"\\n\"
    
    lang_display = CONFIG.get(lang_key, {}).get('name', lang_key.upper())
    
    # Status line
    if winner:
        if winner == 'draw':
            status = f\"🏁 **Result: Draw! ({lang_display})**\"
        else:
            status = f\"🏆 **Winner: {winner} ({lang_display})**\"
        
        # Add reset link if game over
        reset_title = f\"{lang_display}: Tic-Tac-Toe: Reset\"
        reset_url = f\"https://github.com/{owner}/{repo}/issues/new?title={quote_plus(reset_title)}&body=Reset+the+board\"
        status += f\" [🔄 Reset]({reset_url})\"
    else:
        status = f\"🎮 **Next Move: {turn} ({lang_display})**\"
            
    log_md = \"\"
    if state.get('log'):
        log_md = \"\\n\\n### 📝 Move History\\n\"
        # Only show last 10 moves to keep it concise
        moves = state['log'][-10:]
        if len(state['log']) > 10:
            log_md += \"... (older moves hidden) ...\\n\"
        for i, move in enumerate(moves):
            log_md += f\"{i+1}. {move['player']} at {move['cell']}\\n\"
            
    # Technical Details
    tech_details = f\"\\n<details>\\n<summary>🛠️ <b>Technical Details (Code & IO)</b></summary>\\n\\n\"
    tech_details += f\"### 🛰️ Execution Context\\n```json\\n{json.dumps(state, indent=2)}\\n```\\n\\n\"
    tech_details += f\"### 💻 Implementation Code ({lang_display})\\n\"
    tech_details += f\"``` {lang_key}\\n\"
    code_content = get_source_code(lang_key)
    tech_details += f\"{code_content}\\n\"
    tech_details += \"```\\n\"
    tech_details += \"</details>\"
    
    return f\"{board_md}\\n\\n{status}{log_md}\\n{tech_details}\"
