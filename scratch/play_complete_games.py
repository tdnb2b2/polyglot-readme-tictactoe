import os
import json
import subprocess
import sys

# Add current dir to path to import shared
sys.path.append(os.getcwd())
from shared.board import CELL_TO_IDX

LANGUAGES = [
    'python', 'javascript', 'typescript', 'go', 'rust',
    'java', 'kotlin', 'php', 'ruby', 'csharp', 
    'c', 'cpp', 'scala', 'swift'
]

def get_empty_cells(board):
    cells = []
    for ri, row in enumerate(board):
        for ci, val in enumerate(row):
            if not val:
                cells.append(f"{['A','B','C'][ci]}{ri+1}")
    return cells

def play_game(lang):
    print(f"=== Playing game for {lang} ===")
    
    # Reset first
    os.environ['ISSUE_TITLE'] = f"{lang}: Tic-Tac-Toe: Reset"
    os.environ['GITHUB_TOKEN'] = 'fake_token'
    os.environ['REPO'] = 'owner/repo'
    os.environ['ISSUE_NUMBER'] = '1'
    
    # Mock _close_issue in dispatcher to prevent API errors
    # Actually, I'll just run it and catch the error or mock it.
    
    while True:
        with open('game_state.json', 'r') as f:
            all_states = json.load(f)
        
        state = all_states.get(lang)
        if state['winner'] or all(all(row) for row in state['board']):
            print(f"Game finished for {lang}. Result: {state['winner'] or 'Draw'}")
            break
        
        empty = get_empty_cells(state['board'])
        if not empty:
            break
            
        next_cell = empty[0] # Just take the first available
        os.environ['ISSUE_TITLE'] = f"{lang}: Tic-Tac-Toe: Put {next_cell}"
        
        print(f"  Move: {state['turn']} at {next_cell}")
        
        # Run dispatcher
        # We need to mock the API call in dispatcher or just let it fail silently
        # since we already updated the README locally.
        try:
            subprocess.run(['python3', 'dispatcher.py', 'run'], 
                           env=os.environ, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            # It might fail at _close_issue (API call), but we care about the files
            pass

def main():
    for lang in LANGUAGES:
        try:
            play_game(lang)
        except Exception as e:
            print(f"Failed to play game for {lang}: {e}")

if __name__ == "__main__":
    main()
