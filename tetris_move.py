from pydantic import BaseModel

class Move(BaseModel):
    rotation: int
    horizontal_movement: int

class MoveQuality(BaseModel):
    air_below: int
    elevation: int
    max_height: int