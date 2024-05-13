from datetime import datetime
from uuid import UUID
from typing import Any, Optional
from pydantic import BaseModel, Json, field_validator


class Question(BaseModel):
    id: UUID
    title: str
    name: str
    survey_id: UUID
    options: list[str] | None
    answers: str
    recommendation: str


class Recomendation(BaseModel):
    title: str
    recomendation: str


class RecomendationView(BaseModel):
    recomendations: list[Recomendation] | None


class Result(BaseModel):
    id: UUID
    user_id: UUID
    survey_id: UUID
    correct_answers: list[UUID]
    answers_amount: int
    survey_len: int


class Survey(BaseModel):

    id: UUID
    title: str
    questions: list[Question] | None
    survey_json: Optional[dict]
    published: bool


class QuestionCreate(BaseModel):
    title: str
    name: str
    options: list[str] | None
    answers: str
    recommendation: str


class SurveyCreate(BaseModel):
    title: str
    questions: list[QuestionCreate] | None
    survey_json: Optional[dict]


class ResultCreate(BaseModel):
    survey_id: UUID
    answers: dict


class User(BaseModel):
    username: str


class SurveyTitle(BaseModel):
    id: UUID
    title: str


class ResultDetail(BaseModel):
    id: UUID
    user_id: UUID
    created_at: datetime
    correct_answers: list[UUID]
    answers_amount: int
    survey_len: int
    survey: SurveyTitle
    user: User
