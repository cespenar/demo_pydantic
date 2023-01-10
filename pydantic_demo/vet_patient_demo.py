import json
from datetime import datetime
from pathlib import Path
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, Field


class Pet(BaseModel):
    """Represents a pet"""
    id: UUID = Field(default_factory=uuid4)
    name: str
    species: str
    weight_kg: float = None
    birthday: datetime = None
    allergies: list[str] = None
    chip: bool = None
    chip_number: int = None


class Person(BaseModel):
    """Represent pet's caretaker"""
    id: UUID = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    phone_number: int = None
    email: EmailStr = None
    pets: list[Pet]


if __name__ == '__main__':
    file_name = Path('../data/vet_data.json')
    with file_name.open() as f:
        data = json.load(f)
        print(json.dumps(data, indent=2))
