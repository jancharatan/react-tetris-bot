from tetris_move import Move, MoveQuality, rotation, horizontal_movement
from typing import List

def clean_tile(tile: List[List[str]]) -> List[List[str]]:
    tile_width = max(list(map(lambda t: len(''.join(t).strip()), tile)))
    return list(map(lambda t: t[:tile_width], tile))

def generate_move(board: list[list[str]], next_tile: List[List[str]]) -> Move:
    pass

def try_to_drop(
        horizontal_movement: int, 
        rotation: int, 
        board: List[List[str]], 
        tile: List[List[str]]
    ) -> MoveQuality:
    pass