import os
import json
import subprocess
import sys

# Add current dir to path to import shared
sys.path.append(os.getcwd())

LANGUAGES = [
    'python', 'javascript', 'typescript', 'go', 'rust',
    'ruby', 'c', 'swift'
]

def get_empty_cells(board):
    cells = []
    for ri, row in enumerate(board):
        for ci, val in enumerate(row):
            if not val:
                cells.append(f"{['A','B','C'][ci]}{ri+1}")
    return cells

def play_one_move(lang):
    print(f"--- Playing move for {lang} ---")
    
    with open('game_state.json', 'r') as f:
        all_states = json.load(f)
    
    state = all_states.get(lang)
    if not state:
        print(f"No state for {lang}")
        return

    if state.get('winner') or all(all(row) for row in state['board']):
        print(f"Game finished for {lang}. Resetting...")
        os.environ['ISSUE_TITLE'] = f"{lang}: Tic-Tac-Toe: Reset"
    else:
        empty = get_empty_cells(state['board'])
        if not empty:
            print(f"No empty cells for {lang} but no winner? Resetting...")
            os.environ['ISSUE_TITLE'] = f"{lang}: Tic-Tac-Toe: Reset"
        else:
            # Pick a move
            next_cell = empty[0]
            os.environ['ISSUE_TITLE'] = f"{lang}: Tic-Tac-Toe: Put {next_cell}"
    
    os.environ['GITHUB_TOKEN'] = 'fake'
    os.environ['REPO'] = 'tdnb2b2/polyglot-readme-tictactoe'
    os.environ['ISSUE_NUMBER'] = '1'

    try:
        subprocess.run(['python3', 'dispatcher.py', 'run'], check=True)
        print(f"Success for {lang}")
    except Exception as e:
        print(f"Failed for {lang}: {e}")

def main():
    for lang in LANGUAGES:
        play_one_move(lang)

if __name__ == "__main__":
    main()
