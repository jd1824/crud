from pydantic import BaseModel, ConfigDict
from typing import List, ClassVar

class User(BaseModel):
    id: int | None = None
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True

class User_response(BaseModel):
    message: str | None = None
    id: int | None = None
    name: str
    email: str
    password: str
