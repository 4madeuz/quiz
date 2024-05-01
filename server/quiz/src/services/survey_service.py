import hashlib
from datetime import datetime
from typing import Sequence
from uuid import UUID

from fastapi import Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.db.postgres import get_session
from src.services.postgres_service import PostgresService
from src.schemas.questions import Survey as SurveySchema
from src.schemas.questions import SurveyCreate
from src.schemas.users import User
from src.models.questions import Survey as SurveyModel, Question
from src.core.exeptions import InvalidFieldException


class SurveyService():
    """Сервис для управления URL"""

    def __init__(
        self,
        model_schema_class: type[SurveySchema],
        postgres_service: PostgresService,
        session: AsyncSession,
    ):
        self.model_schema_class = model_schema_class
        self.postgres_service = postgres_service
        self.session = session

    async def create_model(self, model_schema: SurveyCreate) -> SurveyModel:
        try:
            db_model: SurveyModel = await self.postgres_service.create(model_schema)
        except IntegrityError:
            raise InvalidFieldException()
        return db_model

    async def get_model_by_id(self, model_id: UUID) -> SurveyModel:

        db_model: SurveyModel = await self.postgres_service.get_by_id(model_id)

        if not db_model:
            return None

        return db_model

    async def get_all_models(self, user: User) -> Sequence[SurveyModel]:

        if user.is_admin:
            db_models: Sequence[SurveyModel] = await self.session.execute(select(SurveyModel))
            db_models = db_models.unique().scalars().all()
        else:
            db_models = await self.session.execute(
                select(SurveyModel).where(SurveyModel.published is True))
            db_models = db_models.unique().scalars().all()

        return db_models

    async def create_survey(self, survey_data: SurveyCreate) -> SurveyModel:
        survey = SurveyModel(title=survey_data.title, survey_json=survey_data.survey_json)
        self.session.add(survey)

        if survey_data.questions:
            for question_data in survey_data.questions:
                question = Question(
                    title=question_data.title,
                    name=question_data.name,
                    survey_id=survey.id,
                    recommendation=question_data.recommendation,
                    options=question_data.options,
                    answers=question_data.answers,
                    )
                survey.questions.append(question)
        self.session.add(survey)
        await self.session.commit()
        return survey

    async def delete_survey(self, survey_id: str):
        return await self.postgres_service.delete(survey_id)

    async def publish_survey(self, survey_id: str):
        db_model: SurveyModel = await self.postgres_service.get_by_id(survey_id)
        db_model.published = not db_model.published
        self.session.add(db_model)
        await self.session.commit()
        return db_model


def get_survey_service(
    pg_session: AsyncSession = Depends(get_session),
) -> SurveyService:
    return SurveyService(
        model_schema_class=SurveySchema,
        session=pg_session,
        postgres_service=PostgresService(
            session=pg_session, model_class=SurveyModel
        ),
    )
