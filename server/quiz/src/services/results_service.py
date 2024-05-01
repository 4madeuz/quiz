import hashlib
from datetime import datetime
from typing import Sequence
from uuid import UUID

from fastapi import Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased
from sqlalchemy import select

from src.db.postgres import get_session
from src.services.postgres_service import PostgresService
from src.schemas.questions import Result as ResultSchema
from src.schemas.questions import SurveyCreate, ResultCreate, Recomendation, RecomendationView
from src.models.questions import Survey, Result
from src.models.users import User
from src.models.questions import Question, Survey
from src.core.exeptions import InvalidFieldException


class ResultService():
    """Сервис для управления URL"""

    def __init__(
        self,
        model_schema_class: type[ResultSchema],
        postgres_service: PostgresService,
        session: AsyncSession,
    ):
        self.model_schema_class = model_schema_class
        self.postgres_service = postgres_service
        self.session = session

    async def create_model(self, model_schema: SurveyCreate) -> Result: # type: ignore
        try:
            db_model: Result = await self.postgres_service.create(model_schema)# type: ignore
        except IntegrityError:
            raise InvalidFieldException()
        return db_model

    async def get_model_by_id(self, model_id: UUID) -> Result:# type: ignore

        db_model = await self.session.execute(select(Result).where(Result.id == model_id))
        db_model = db_model.scalars().first()

        query = (
            select(Question)
            .filter(
                ~Question.id.in_(db_model.correct_answers),
                Question.survey_id == db_model.survey_id
            )
        )
        result = await self.session.execute(query)
        missing_questions = result.scalars().all()
        result = RecomendationView(recomendations=[])
        for question in missing_questions:
            recomendation = Recomendation(
                title=question.title,
                recomendation=question.recommendation
            )
            result.recomendations.append(recomendation)
        if not db_model:
            return None

        return result

    async def get_all_models(self) -> Sequence[Result]:# type: ignore

        db_models: Sequence[Result] = await self.postgres_service.get_all()# type: ignore

        return db_models

    async def get_users_models(self, user_id: UUID) -> Sequence[Result]:# type: ignore

        db_models = await self.session.execute(select(Result).where(Result.user_id == user_id))
        db_models = db_models.scalars().all()

        return db_models

    async def validate_results(self, result_data: ResultCreate, user: User) -> dict:
        survey = await self.session.get(Survey, result_data.survey_id)
        correct_answers = []
        for question in survey.questions:
            if result_data.answers[question.name] == question.answers:
                correct_answers.append(question.id)
        result = Result(
            user_id=user.id,
            survey_id=survey.id,
            correct_answers=correct_answers,
            answers_amount=len(correct_answers),
            survey_len=len(question.options)
        )
        self.session.add(result)
        await self.session.commit()
        return result.id


def get_result_service(
    pg_session: AsyncSession = Depends(get_session),
) -> ResultService:
    return ResultService(
        model_schema_class=ResultSchema,
        session=pg_session,
        postgres_service=PostgresService(
            session=pg_session, model_class=Result
        ),
    )
