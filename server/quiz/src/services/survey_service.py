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
from src.models.questions import Survey as SurveyModel



class SurveyService():
    """Сервис для управления URL"""

    def __init__(
        self,
        model_schema_class: type[SurveySchema],
        postgres_service: PostgresService,
    ):
        self.model_schema_class = model_schema_class
        self.postgres_service = postgres_service

    async def create_model(self, model_schema: URLCreate) -> URLModel:

        short_url = self._shorten_url(model_schema.original_url)

        schema = URLCreateFull(
            original_url=model_schema.original_url, short_url=short_url,
        )
        try:
            db_model: URLModel = await self.postgres_service.create(schema)
        except IntegrityError:
            raise InvalidFieldException(schema.original_url)
        return db_model


def get_survey_service(
    pg_session: AsyncSession = Depends(get_session),
) -> URLService:
    return URLService(
        model_schema_class=URLSchema,
        postgres_service=PostgresService(
            session=pg_session, model_class=URLModel
        ),
    )
