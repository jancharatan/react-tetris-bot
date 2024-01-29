import pytest
from tetris_algorithm import clean_tile, try_to_drop, rotate_tile
from tetris_move import MoveQuality

def test_clean_tile(square_tile, t_tile):
    assert len(clean_tile(square_tile)[0]) == 2
    assert len(clean_tile(t_tile)[0]) == 3

@pytest.mark.parametrize("rotation", [0, 1, 2, 3])
def test_rotate_square_tile(square_tile, rotation):
    square_tile = clean_tile(square_tile)
    assert rotate_tile(rotation, square_tile) == square_tile

def test_rotate_t_tile(t_tile):
    t_tile = clean_tile(t_tile)
    assert rotate_tile(0, t_tile) == t_tile

def test_rotate_t_tile_90(t_tile):
    t_tile = clean_tile(t_tile)
    assert rotate_tile(1, t_tile) == [["", "c"], ["c", "c"], ["", "c"]]

def test_rotate_t_tile_180(t_tile):
    t_tile = clean_tile(t_tile)
    assert rotate_tile(2, t_tile) == [["c", "c", "c"], ["", "c", ""]]

def test_rotate_t_tile_270(t_tile):
    t_tile = clean_tile(t_tile)
    assert rotate_tile(3, t_tile) == [["c", ""], ["c", "c"], ["c", ""]]

@pytest.mark.xfail
def test_try_to_drop_square_tile(square_tile, simple_board):
    assert try_to_drop(0, 0, simple_board, square_tile) == MoveQuality(air_below=0, max_height=2)