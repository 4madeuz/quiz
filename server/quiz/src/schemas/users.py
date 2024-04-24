from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from src.schemas.questions import Survey


class User(BaseModel):
    id: UUID
    email: str
    username: str
    surveys: list[Survey] | None


class UserCreate(BaseModel):
    email: str
    username: str
