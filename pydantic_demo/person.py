from pydantic import BaseModel, EmailStr

from pet import Pet


class Person(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone_number: int = None
    email: EmailStr = None
    pets: list[Pet]
