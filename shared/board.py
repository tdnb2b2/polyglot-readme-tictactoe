import os
import re
import json
from urllib.parse import quote_plus

SYMBOLS = {'X': '❌', 'O': '⭕', '': '___'}

# Configuration for language display names and runner settings
CONFIG = {
    'python':     {'name': 'Python',     'cmd': ['python3', 'game.py']},
    'javascript': {'name': 'JavaScript', 'cmd': ['node', 'game.js']},
    'typescript': {'name': 'TypeScript', 'cmd': ['npm', 'run', 'play']},
    'go':         {'name': 'Go',         'cmd': ['go', 'run', 'game.go']},
    'rust':       {'name': 'Rust',       'cmd': ['cargo', 'run', '--release']},
    'java':       {'name': 'Java',       'cmd': ['java', 'Game']},
    'kotlin':     {'name': 'Kotlin',     'cmd': ['java', '-jar', 'Game.jar']},
    'php':        {'name': 'PHP',        'cmd': ['php', 'game.php']},
    'ruby':       {'name': 'Ruby',       'cmd': ['ruby', 'game.rb']},
    'csharp':     {'name': 'C#',         'cmd': ['dotnet', 'run', '--no-build']},
    'c':          {'name': 'C',          'cmd': ['./game']},
    'cpp':        {'name': 'C++',        'cmd': ['./game']},
    'scala':      {'name': 'Scala',      'cmd': ['scala', 'Game.scala']},
    'swift':      {'name': 'Swift',      'cmd': ['swift', 'game.swift']},
}

def clean_source_code(content):
    """
    Sanitizes source code for safe Markdown embedding.
    Removes null bytes and escapes backticks.
    """
    if not content: return ""
    # Remove null bytes which can break regex/rendering
    content = content.replace('\x00', '')
    # Escape backticks to prevent breaking triple-backtick code blocks
    content = content.replace('```', '` ` `')
    return content

def get_source_code(lang_key):
    """Retrieves and sanitizes source code for a given language."""
    lang_file_map = {
        'python': 'game.py', 'javascript': 'game.js', 'typescript': 'game.ts',
        'go': 'game.go', 'rust': 'src/main.rs', 'java': 'Game.java',
        'kotlin': 'game.kt', 'php': 'game.php', 'ruby': 'game.rb',
        'csharp': 'Program.cs', 'c': 'game.c', 'cpp': 'game.cpp',
        'scala': 'game.scala', 'swift': 'game.swift'
    }
    
    filename = lang_file_map.get(lang_key)
    if not filename:
        return f"// Source for {lang_key} not found."
        
    path = os.path.join('implementations', lang_key, filename)
    if not os.path.exists(path):
        return f"// File {path} not found."
        
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
            return clean_source_code(content)
    except Exception as e:
        return f"// Error reading source for {lang_key}: {str(e)}"

def get_source_code_link(lang_key):
    """Returns a link to the source code file instead of the full content."""
    lang_file_map = {
        'python': 'game.py', 'javascript': 'game.js', 'typescript': 'game.ts',
        'go': 'game.go', 'rust': 'src/main.rs', 'java': 'Game.java',
        'kotlin': 'game.kt', 'php': 'game.php', 'ruby': 'game.rb',
        'csharp': 'Program.cs', 'c': 'game.c', 'cpp': 'game.cpp',
        'scala': 'game.scala', 'swift': 'game.swift'
    }
    filename = lang_file_map.get(lang_key, "")
    if not filename: return ""
    return f"https://github.com/tdnb2b2/polyglot-readme-tictactoe/blob/main/implementations/{lang_key}/{filename}"

def replace_section(content, name, new_section):
    """
    Replaces a section in content marked by <!-- NAME_START --> and <!-- NAME_END -->
    Uses a lambda for replacement to avoid any backslash interpolation issues.
    """
    pattern = rf"(<!-- {name}_START -->).*?(<!-- {name}_END -->)"
    try:
        return re.sub(pattern, lambda m: f"{m.group(1)}\n\n{new_section}\n\n{m.group(2)}", content, flags=re.DOTALL)
    except Exception as e:
        print(f"Error in replace_section for {name}: {e}")
        return content

def render_board_md(lang_key, state, owner="tdnb2b2", repo="polyglot-readme-tictactoe"):
    """
    Renders the Tic-Tac-Toe board as a robust HTML table with interactive Badge links.
    """
    board = state.get('board', [['']*3 for _ in range(3)])
    turn = state.get('turn', 'X')
    winner = state.get('winner')
    log = state.get('log', [])
    
    lang_display = CONFIG.get(lang_key, {}).get('name', lang_key.upper())
    safe_lang = lang_display.replace('+', '%2B').replace('#', '%23')

    # Status Message
    if winner:
        if winner == "draw":
            status = "🤝 **It's a Draw!**"
        else:
            status = f"🏆 **Winner: {winner} ({lang_display})**"
    else:
        status = f"🎮 **Next Move: {turn} ({lang_display})**"

    # HTML Table Construction
    html = ['<table align="center">', '  <thead>', '    <tr>', '      <th></th>', '      <th>A</th>', '      <th>B</th>', '      <th>C</th>', '    </tr>', '  </thead>', '  <tbody>']
    
    BADGE_BASE = "https://img.shields.io/badge/"
    STYLE = "?style=for-the-badge"
    
    for r in range(3):
        row_num = r + 1
        html.append('    <tr>')
        html.append(f'      <td align="center"><b>{row_num}</b></td>')
        for c in range(3):
            cell_val = board[r][c]
            cell_id = f"{['A','B','C'][c]}{row_num}"
            
            content = ""
            if cell_val == 'X':
                content = f'<img src="{BADGE_BASE}-X-red{STYLE}" alt="X">'
            elif cell_val == 'O':
                content = f'<img src="{BADGE_BASE}-O-blue{STYLE}" alt="O">'
            elif winner:
                content = f'<img src="{BADGE_BASE}-%20-lightgrey{STYLE}" alt=" ">'
            else:
                title = f"{safe_lang}: Tic-Tac-Toe: Put {cell_id}"
                url = f'https://github.com/{owner}/{repo}/issues/new?title={quote_plus(title)}&body=Play+{quote_plus(lang_display)}+board'
                content = f'<a href="{url}"><img src="{BADGE_BASE}-{cell_id}-grey{STYLE}" alt="{cell_id}"></a>'
            
            html.append(f'      <td align="center">{content}</td>')
        html.append('    </tr>')
    
    html.append('  </tbody>')
    html.append('</table>')
    
    board_html = '\n'.join(html)

    # Footer Info
    log_md = ""
    if log:
        recent = log[-5:]
        log_md = '\n\n**Recent history:** ' + ' → '.join(f'`{e["player"]} {e["cell"]}`' for e in recent)

    source_link = get_source_code_link(lang_key)
    footer = f"\n\n{status}{log_md}\n\n---\n[📄 View {lang_display} Implementation]({source_link}) | [🔄 Reset Board](https://github.com/{owner}/{repo}/issues/new?title={safe_lang}%3A+Tic--Tac--Toe%3A+Reset&body=Reset+{quote_plus(lang_display)}+board)"

    return f"{board_html}\n{footer}"
