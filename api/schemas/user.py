# -*- coding: utf-8 -*-
from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr

# from pydantic.types import UUID4


class UserBase(BaseModel):
    name: str
    birth_date: date
    email: EmailStr
    is_admin: bool


class User(UserBase):
    # id: UUID4
    id: int


class UserCreate(UserBase):
    password: str


class UserRead(User):
    pass


class UserUpdate(UserBase):
    # id: UUID4
    id: int
    name: Optional[str]
    birth_date: Optional[date]
    email: Optional[EmailStr]
    password: Optional[str]
    is_admin: Optional[bool]