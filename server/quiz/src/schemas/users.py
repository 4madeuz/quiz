from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    email: str
    username: str


class UserCreate(BaseModel):
    email: str
    username: str
    password: str
    is_admin: bool


class UserShort(BaseModel):
    id: UUID
    email: str
    username: str
    is_admin: bool


class TokenData(BaseModel):
    username: str | None
    is_admin: bool
