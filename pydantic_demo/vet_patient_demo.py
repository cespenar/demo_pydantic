from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, Field


class Pet(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    species: str
    weight: float = None
    birthday: datetime = None
    allergies: list[str] = None
    chipped: bool = None
    chip_number: int = None


class Person(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    phone_number: int = None
    email: EmailStr = None
    pets: list[Pet]


if __name__ == '__main__':
    pass
