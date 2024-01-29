from pydantic import BaseModel

class Move(BaseModel):
    rotation: int
    x_start: int

class MoveQuality(BaseModel):
    air_below: int
    elevation: int