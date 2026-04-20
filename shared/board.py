import os
import json
import re

# Simple 3x3 Tic-Tac-Toe board state mapping
CELL_TO_IDX = {
    'A1': (0, 0), 'B1': (0, 1), 'C1': (0, 2),
    'A2': (1, 0), 'B2': (1, 1), 'C2': (1, 2),
    'A3': (2, 0), 'B3': (2, 1), 'C3': (2, 2)
}

def get_source_code_link(lang_key: str) -> str:
    """Returns a link to the source code file instead of the full content."""
    lang_file_map = {
        'python': 'game.py', 'javascript': 'game.js', 'typescript': 'game.ts',
        'go': 'game.go', 'rust': 'src/main.rs', 'java': 'Game.java',
        'kotlin': 'Game.kt', 'php': 'game.php', 'ruby': 'game.rb',
        'csharp': 'Program.cs', 'c': 'game.c', 'cpp': 'game.cpp',
        'scala': 'Game.scala', 'swift': 'game.swift'
    }
    filename = lang_file_map.get(lang_key, "")
    if not filename: return ""
    # Hardcoded link to the main repo for stability
    return f"https://github.com/tdnb2b2/polyglot-readme-tictactoe/blob/main/implementations/{lang_key}/{filename}"

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
    return pattern.sub(f"{start_tag}\n\n{replacement}\n\n{end_tag}", content)

def render_board_md(board: list, lang_key: str, owner: str, repo: str,
                    turn: str, winner: str, log: list, 
                    input_info: str = "", output_info: str = "") -> str:
    """
    Renders the Tic-Tac-Toe board as a robust HTML table with interactive Badge links.
    """
    LANG_DISPLAY = {
        'python': 'Python', 'javascript': 'JavaScript', 'typescript': 'TypeScript',
        'go': 'Go', 'rust': 'Rust', 'java': 'Java', 'kotlin': 'Kotlin',
        'php': 'PHP', 'ruby': 'Ruby', 'csharp': 'C#', 'c': 'C',
        'cpp': 'C++', 'scala': 'Scala', 'swift': 'Swift',
    }
    lang_display = LANG_DISPLAY.get(lang_key, lang_key)
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
                content = f'<img src="{BADGE_BASE}- -lightgrey{STYLE}" alt=" ">'
            else:
                issue_title = f"{safe_lang}%3A+Tic-Tac-Toe%3A+Put+{cell_id}"
                url = f'https://github.com/{owner}/{repo}/issues/new?title={issue_title}&body=Play+{safe_lang}+board'
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
    footer = f"\n\n{status}{log_md}\n\n---\n[📄 View {lang_display} Implementation]({source_link}) | [🔄 Reset Board](https://github.com/{owner}/{repo}/issues/new?title={safe_lang}%3A+Tic-Tac-Toe%3A+Reset&body=Reset+safe_lang+board)"

    return f"{board_html}\n{footer}"
