from math import inf
from typing import List
from tetris_move import Move, MoveQuality

def clean_tile(tile: List[List[str]]) -> List[List[str]]:
    tile_width = max(list(map(lambda t: len(''.join(t).strip()), tile)))
    return list(map(lambda t: t[:tile_width], tile))

def generate_move(board: list[list[str]], tile: List[List[str]]) -> Move:
    current_move_quality = current_move = None
    tile = clean_tile(tile)
    for rotation in [0, 1, 2, 3]:
        current_tile = clean_tile(rotate_tile(rotation, tile))
        for x_index in range(0, len(board[0]) - len(current_tile[0])):
            attempt = try_to_drop(board, current_tile, x_index)
            if (not current_move_quality) or (attempt.air_below <= current_move_quality.air_below and attempt.elevation < current_move_quality.elevation):
                current_move_quality = attempt
                current_move = Move(rotation=rotation, x_start=x_index)
    return current_move

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

def max_height_of_given_at_x(board_or_tile: List[List[str]], x: int, given: str = "c") -> int:
    count = 0
    for i in range(len(board_or_tile) - 1, -1, -1):
        if board_or_tile[i][x] != given:
            return count
        count += 1
    return count

def get_x_start(board_width: int, tile_width: int) -> int:
    return (board_width // 2 - 1) - (tile_width // 4)

def get_lowest_elevation(board: List[List[str]], tile: List[List[str]], x_index: int) -> int:
    curr_min = -inf
    for i in range(len(tile[0])):
        max_height = max_height_of_given_at_x(board, x_index + i)
        air_below_height = max_height_of_given_at_x(tile, i, "")
        curr_min = max(curr_min, max_height - air_below_height)
    return curr_min

def get_total_air_below(board: List[List[str]], tile: List[List[str]], x_index: int, height: int) -> int:
    air_below = 0
    for i in range(len(tile[0])):
        max_height = max_height_of_given_at_x(board, x_index + i)
        air_below += height - max_height
    return air_below

def try_to_drop(board: List[List[str]], tile: List[List[str]], x_index: int) -> MoveQuality:
    lowest_elevation = get_lowest_elevation(board, tile, x_index)
    total_air_below = get_total_air_below(board, tile, x_index, lowest_elevation)
    return MoveQuality(air_below=total_air_below, elevation=lowest_elevation)
    
