import pytest
from tetris_algorithm import clean_tile, try_to_drop
from tetris_move import MoveQuality

def test_clean_tile(square_tile, t_tile):
    assert len(clean_tile(square_tile)[0]) == 2
    assert len(clean_tile(t_tile)[0]) == 3

@pytest.mark.xfail
def test_try_to_drop_square_tile(square_tile, simple_board):
    assert try_to_drop(0, 0, simple_board, square_tile) == MoveQuality(air_below=0, max_height=2)