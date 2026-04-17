import json, os, sys, re

# Shared utilities for cell conversion and winner detection
CELL_TO_IDX = {
    'A1': (0, 0), 'A2': (0, 1), 'A3': (0, 2),
    'B1': (1, 0), 'B2': (1, 1), 'B3': (1, 2),
    'C1': (2, 0), 'C2': (2, 1), 'C3': (2, 2)
}

def check_winner(board):
    # Rows, Cols, Diagonals
    lines = [
        [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]
    ]
    for line in lines:
        values = [board[r][c] for r, c in line]
        if values[0] != '' and all(v == values[0] for v in values):
            return values[0]
    return None

def is_draw(board):
    return all(all(cell != '' for cell in row) for row in board)

def render_board_table(board, lang_name):
    # Generate the Markdown table for the given board
    lines = []
    lines.append("|   | 1 | 2 | 3 |")
    lines.append("|---|---|---|---|")
    
    rows = ['A', 'B', 'C']
    for i, row_label in enumerate(rows):
        cells = []
        for j in range(3):
            val = board[i][j]
            if val == 'X':
                cells.append("❌")
            elif val == 'O':
                cells.append("⭕")
            else:
                cell_id = f"{row_label}{j+1}"
                issue_url = f"https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title={lang_name.replace('+', '%2B').replace('#', '%23')}%3A+Tic-Tac-Toe%3A+Put+{cell_id}&body=Play+{lang_name}+board"
                cells.append(f"[➕]({issue_url})")
        lines.append(f"| **{row_label}** | {' | '.join(cells)} |")
    return "\n".join(lines)
