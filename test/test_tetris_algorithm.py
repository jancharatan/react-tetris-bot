import pytest
from tetris_algorithm import clean_tile, try_to_drop, rotate_tile, max_height_at_x
from tetris_move import MoveQuality

def test_clean_tile(square_tile, t_tile):
    assert len(clean_tile(square_tile)[0]) == 2
    assert len(clean_tile(t_tile)[0]) == 3

@pytest.mark.parametrize("rotation", [0, 1, 2, 3])
def test_rotate_square_tile(square_tile, rotation):
    square_tile = clean_tile(square_tile)
    assert rotate_tile(rotation, square_tile) == square_tile

@pytest.mark.parametrize("rotation, expected", [
    (0, [["", "c", ""], ["c", "c", "c"]]), 
    (1, [["", "c"], ["c", "c"], ["", "c"]]), 
    (2, [["c", "c", "c"], ["", "c", ""]]), 
    (3, [["c", ""], ["c", "c"], ["c", ""]])
])
def test_rotate_t_tile(t_tile, rotation, expected):
    t_tile = clean_tile(t_tile)
    assert rotate_tile(rotation, t_tile) == expected

@pytest.mark.parametrize("x_index, max_height", [(0, 1), (1, 2), (2, 2), (3, 1), (4, 0)])
def test_max_height_at_x(simple_board, x_index, max_height):
    assert max_height_at_x(simple_board, x_index) == max_height

@pytest.mark.xfail
def test_try_to_drop_square_tile(square_tile, simple_board):
    assert try_to_drop(0, 0, simple_board, square_tile) == MoveQuality(air_below=0, max_height=2)