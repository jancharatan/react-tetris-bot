from pydantic import BaseModel

rotation = [0, 1, 2, 3]
horizontal_movement = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

class Move(BaseModel):
    rotation: int
    horizontal_movement: int

class MoveQuality(BaseModel):
    air_below: int
    max_height: int