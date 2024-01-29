import pytest

@pytest.fixture
def square_tile():
    return [
        ["c", "c", "", ""],
        ["c", "c", "", ""]
    ]

@pytest.fixture
def t_tile():
    return [
        ["", "c", "", ""],
        ["c", "c", "c", ""]
    ]

@pytest.fixture
def empty_row():
    return [""] * 20

@pytest.fixture
def simple_board(empty_row):
    board = [empty_row] * 18
    board.append(["", "c", "c", "", "", "", "", "", "", ""])
    board.append(["c", "c", "c", "c", "", "", "", "", "", ""])
    return board
