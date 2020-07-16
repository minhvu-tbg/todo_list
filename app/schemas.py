from typing import List, Optional

from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_done: Optional[bool] = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    owner_id: int = None

    class Config:
        orm_mode = True


class Todo(TodoBase):
    id: int
    owner_id: int = None

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    is_active: bool
    items: List[Todo] = []

    class Config:
        orm_mode = True
