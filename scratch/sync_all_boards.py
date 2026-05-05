import os
import sys
import json
import re

# Add root to sys.path to import shared.board
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.board import render_board_md

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(ROOT, 'README.md')
STATE_PATH = os.path.join(ROOT, 'game_state.json')

LANGS = {
    "c": "C",
    "cpp": "C++",
    "csharp": "C#",
    "go": "Go",
    "java": "Java",
    "javascript": "JavaScript",
    "kotlin": "Kotlin",
    "php": "PHP",
    "python": "Python",
    "ruby": "Ruby",
    "rust": "Rust",
    "scala": "Scala",
    "swift": "Swift",
    "typescript": "TypeScript"
}

def main():
    with open(STATE_PATH, 'r') as f:
        all_state = json.load(f)

    with open(README_PATH, 'r') as f:
        readme = f.read()

    for lang_key, lang_display in LANGS.items():
        state = all_state.get(lang_key)
        if not state:
            print(f"Skipping {lang_key}: no state found.")
            continue
        
        # Render current board
        board_md = render_board_md(
            state.get('board', [['','',''],['','',''],['','','']]),
            lang_key,
            "tdnb2b2",
            "polyglot-readme-tictactoe",
            state.get('turn', 'X'),
            state.get('winner'),
            state.get('log', []),
            input_info=state.get('last_input', ''),
            output_info=state.get('last_output', '')
        )
        
        # Replace in README
        marker_start = f'<!-- BOARD_{lang_key.upper()}_START -->'
        marker_end = f'<!-- BOARD_{lang_key.upper()}_END -->'
        
        pattern = re.compile(f'{re.escape(marker_start)}.*?{re.escape(marker_end)}', re.DOTALL)
        replacement = f'{marker_start}\n{board_md}\n{marker_end}'
        
        if pattern.search(readme):
            # Use a lambda to prevent re.sub from interpreting backslashes as backreferences
            readme = pattern.sub(lambda m: replacement, readme)
            print(f"Updated {lang_display} board in README.")
        else:
            print(f"Marker not found for {lang_display}.")

    with open(README_PATH, 'w') as f:
        f.write(readme)
    print("DONE.")

if __name__ == '__main__':
    main()
