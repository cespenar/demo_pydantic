from datetime import datetime

from pydantic import BaseModel


class Pet(BaseModel):
    id: int
    name: str
    species: str
    weight: float = None
    birthday: datetime = None
    allergies: list[str] = None
