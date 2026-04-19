import json
import os
import re
from shared.board import render_board_md, replace_section, update_readme_local

LANGS = [
    'c', 'cpp', 'csharp', 'go', 'java', 'javascript', 'kotlin',
    'php', 'python', 'ruby', 'rust', 'scala', 'swift', 'typescript'
]

def refresh_all():
    with open('game_state.json', 'r') as f:
        all_states = json.load(f)
    
    with open('README.md', 'r') as f:
        readme_content = f.read()
    
    owner = 'tdnb2b2'
    repo = 'polyglot-readme-tictactoe'
    
    for lang in LANGS:
        state = all_states.get(lang)
        if not state:
            print(f"Skipping {lang}, state not found")
            continue
        
        print(f"Rendering board for {lang}...")
        new_board_md = render_board_md(
            state['board'], lang, owner, repo,
            state['turn'], state['winner'], state['log']
        )
        
        tag = f"BOARD_{lang.upper()}"
        readme_content = replace_section(readme_content, tag, new_board_md)
    
    update_readme_local(readme_content)
    print("README.md refreshed with all boards.")

if __name__ == "__main__":
    refresh_all()
