from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class Option(BaseModel):
    id: UUID
    text: str
    is_correct: int
    question_id: UUID


class Question(BaseModel):
    id: UUID
    text: str
    survey_id: int
    question_id: UUID
    options: list[Option] | None


class User(BaseModel):
    id: UUID
    username: str
    email: str


class Survey(BaseModel):

    id: UUID
    title: str
    questions: list[Question] | None
    users: list[datetime] | None


class SurveyCreate(BaseModel):
    title: str
    questions: list[Question] | None
    users: list[datetime] | None

