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
def straight_line_tile():
    return [
        ["", "", "", ""],
        ["c", "c", "c", "c"]
    ]

@pytest.fixture
def empty_row():
    return [""] * 10

@pytest.fixture
def simple_board(empty_row):
    board = [empty_row] * 18
    board.append(["", "c", "c", "", "", "", "", "", "", ""])
    board.append(["c", "c", "c", "c", "", "", "", "", "", ""])
    return board

@pytest.fixture
def simple_board_v2(empty_row):
    board = [empty_row] * 18
    board.append(["", "c", "c", "", "", "", "", "", "", ""])
    board.append(["c", "c", "", "", "", "", "", "", "", ""])
    return board

@pytest.fixture
def complex_board(empty_row):
    board = [empty_row] * 17
    board.append(["", "c", "c", "c", "c", "c", "", "", "", ""])
    board.append(["", "c", "c", "c", "", "", "c", "", "", ""])
    board.append(["", "c", "c", "c", "", "", "", "c", "", "c"])
    return board

@pytest.fixture
def straight_line_board(empty_row):
    board = [empty_row] * 16
    board.append(["c", "c", "c", "c", "c", "c", "", "c", "c", "c"])
    board.append(["c", "c", "c", "c", "c", "c", "", "c", "c", "c"])
    board.append(["c", "c", "c", "c", "c", "c", "", "c", "c", "c"])
    board.append(["c", "c", "c", "c", "c", "c", "", "c", "c", "c"])
    return board
