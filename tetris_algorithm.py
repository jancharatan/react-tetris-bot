from tetris_move import Move, MoveQuality, rotation, horizontal_movement
from typing import List

def clean_tile(tile: List[List[str]]) -> List[List[str]]:
    tile_width = max(list(map(lambda t: len(''.join(t).strip()), tile)))
    return list(map(lambda t: t[:tile_width], tile))

def generate_move(board: list[list[str]], next_tile: List[List[str]]) -> Move:
    tile = clean_tile(next_tile)
    for horizontal in horizontal_movement:
        for rot in rotation:
            move_quality = try_to_drop(horizontal, rot, board, tile)
            print(move_quality)

    move = Move(
        horizontal_movement = 4,
        rotation = 0
    )
    return move

def try_to_drop(
        horizontal_movement: int, 
        rotation: int, 
        board: List[List[str]], 
        tile: List[List[str]]
    ) -> MoveQuality:
    pass
