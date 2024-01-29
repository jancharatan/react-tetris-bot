import pytest
from tetris_algorithm import *
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
def test_max_height_of_given_at_x(simple_board, x_index, max_height):
    assert max_height_of_given_at_x(simple_board, x_index) == max_height

@pytest.mark.parametrize("tile_width,x_start", [(4, 3), (3, 4), (2, 4), (1, 4)])
def test_get_x_start(tile_width, x_start):
    assert get_x_start(10, tile_width) == x_start

@pytest.mark.parametrize("x_start,lowest_depth", [(0, 2), (1, 2), (2, 2), (3, 1), (4, 0), (5, 0)])
def test_get_lowest_elevation_t_tile(simple_board, t_tile, x_start, lowest_depth):
    t_tile = clean_tile(t_tile)
    assert get_lowest_elevation(simple_board, t_tile, x_start) == lowest_depth

@pytest.mark.parametrize("x_start,lowest_depth", [(0, 2), (1, 2), (2, 1), (3, 0), (4, 0), (5, 0)])
def test_get_lowest_elevation_t_tile_rotated(simple_board, t_tile, x_start, lowest_depth):
    t_tile = clean_tile(rotate_tile(1, clean_tile(t_tile)))
    assert get_lowest_elevation(simple_board, t_tile, x_start) == lowest_depth

@pytest.mark.parametrize("x_start,height,air_below", [(0, 2, 1), (1, 2, 1), (2, 2, 3), (3, 1, 2), (4, 0, 0)])
def test_get_total_air_below(simple_board, t_tile, x_start, height, air_below):
    t_tile = clean_tile(t_tile)
    assert get_total_air_below(simple_board, t_tile, x_start, height) == air_below

def test_try_to_drop_square_tile(simple_board, square_tile):
    square_tile = clean_tile(square_tile)
    move_quality = try_to_drop(simple_board, square_tile, 0)
    assert move_quality.air_below == 1
    assert move_quality.elevation == 2

def test_generate_move_square_tile(simple_board, square_tile):
    move = generate_move(simple_board, square_tile)
    assert move == Move(rotation=0, x_start=4)

def test_generate_move_t_tile(simple_board, t_tile):
    move = generate_move(simple_board, t_tile)
    assert move == Move(rotation=0, x_start=4)