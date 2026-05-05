import pytest
from shared.board import render_board_md

def make_board(size=3):
    return [[None for _ in range(size)] for _ in range(size)]

def test_render_accepts_legacy_string_logs():
    board = make_board()
    logs = ["X -> A1", "O -> B2", "Draw"]
    out = render_board_md(board, logs)
    assert isinstance(out, str)
    assert out != ""

def test_render_accepts_structured_logs():
    board = make_board()
    logs = [{"player": "X", "cell": "A1"}, {"player": "O", "cell": "B2"}]
    out = render_board_md(board, logs)
    assert isinstance(out, str)
    assert out != ""
