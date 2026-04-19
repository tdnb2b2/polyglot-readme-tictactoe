import json
import os
import re

LANGS = [
    'c', 'cpp', 'csharp', 'go', 'java', 'javascript', 'kotlin',
    'php', 'python', 'ruby', 'rust', 'scala', 'swift', 'typescript'
]

def init_state():
    state = {}
    for lang in LANGS:
        state[lang] = {
            "board": [["", "", ""], ["", "", ""], ["", "", ""]],
            "turn": "X",
            "winner": None,
            "log": []
        }
    with open('game_state.json', 'w') as f:
        json.dump(state, f, indent=2)
    print("Initialized game_state.json")

def init_readme():
    with open('README.md', 'r') as f:
        content = f.read()
    
    # We want to clear out existing board sections and put all 14 languages.
    # For simplicity, we'll recreate the core part of README.
    
    new_content = "# Polyglot Tic-Tac-Toe\n\n"
    new_content += "This is a technical demo repository showing Tic-Tac-Toe implemented in 14 different languages. Each board is independently playable via GitHub Issues.\n\n"
    
    for lang in LANGS:
        title = lang.upper()
        if lang == 'cpp': title = 'C++'
        if lang == 'csharp': title = 'C#'
        
        new_content += f"## {title}\n"
        new_content += f"<!-- BOARD_{lang.upper()}_START -->\n"
        new_content += f"Board for {title} will appear here.\n"
        new_content += f"<!-- BOARD_{lang.upper()}_END -->\n\n"
    
    with open('README.md', 'w') as f:
        f.write(new_content)
    print("Initialized README.md with placeholders")

if __name__ == "__main__":
    init_state()
    init_readme()
