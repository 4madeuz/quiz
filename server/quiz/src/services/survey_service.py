import hashlib
from datetime import datetime
from typing import Sequence
from uuid import UUID

from fastapi import Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.postgres import get_session
from src.services.postgres_service import PostgresService
from src.schemas.questions import Survey as SurveySchema
from src.schemas.questions import SurveyCreate
from src.models.questions import Survey as SurveyModel
from src.core.exeptions import InvalidFieldException



class SurveyService():
    """Сервис для управления URL"""

    def __init__(
        self,
        model_schema_class: type[SurveySchema],
        postgres_service: PostgresService,
    ):
        self.model_schema_class = model_schema_class
        self.postgres_service = postgres_service

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

    async def get_all_models(self) -> Sequence[SurveyModel]:

        db_models: Sequence[SurveyModel] = await self.postgres_service.get_all()

        return db_models


def get_survey_service(
    pg_session: AsyncSession = Depends(get_session),
) -> SurveyService:
    return SurveyService(
        model_schema_class=SurveySchema,
        postgres_service=PostgresService(
            session=pg_session, model_class=SurveyModel
        ),
    )
