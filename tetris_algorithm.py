from tetris_move import Move, MoveQuality, rotation, horizontal_movement
from typing import List

def clean_tile(tile: List[List[str]]) -> List[List[str]]:
    tile_width = max(list(map(lambda t: len(''.join(t).strip()), tile)))
    return list(map(lambda t: t[:tile_width], tile))

def generate_move(board: list[list[str]], tile: List[List[str]]) -> Move:
    tile = clean_tile(tile)
    for horizontal in horizontal_movement:
        for rot in rotation:
            move_quality = try_to_drop(horizontal, rot, board, tile)
            print(move_quality)

    move = Move(
        horizontal_movement = 4,
        rotation = 0
    )
    return move

def rotate_tile(rotation: int, tile: List[List[str]]) -> List[List[str]]:
    if rotation % 4 == 0:
        return tile
    elif rotation % 4 == 1:
        return list(map(list, zip(list(reversed(tile[0])), list(reversed(tile[1])))))
    elif rotation % 4 == 2:
        return [list(reversed(tile[1])), list(reversed(tile[0]))]
    elif rotation % 4 == 3:
        return list(map(list, zip(tile[1], tile[0])))
    raise ValueError("Rotation value must be a 0, 1, 2, 3 (or one of these values when we mod by four)")

def max_height_at_x(board: List[List[str]], x: int) -> int:
    count = 0
    for i in range(len(board) - 1, -1, -1):
        if not board[i][x]:
            return count
        count += 1
    return count

def get_x_start(board_width: int, tile_width: int) -> int:
    return (board_width // 2 - 1) - (tile_width // 4)

def try_to_drop(
        horizontal_movement: int, 
        rotation: int, 
        board: List[List[str]], 
        tile: List[List[str]]
    ) -> MoveQuality:
    tile = clean_tile(rotate_tile(rotation, tile))
    x_start = get_x_start(len(board[0]), len(tile[0]))
