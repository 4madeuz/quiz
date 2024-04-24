import hashlib
from datetime import datetime
from typing import Sequence
from uuid import UUID

from fastapi import Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.postgres import get_session
from src.services.postgres_service import PostgresService
from src.schemas.users import User as UserSchema
from src.schemas.users import UserCreate
from src.models.users import User as UserModel
from src.core.exeptions import InvalidFieldException


class UserService():
    """Сервис для управления URL"""

    def __init__(
        self,
        model_schema_class: type[UserSchema],
        postgres_service: PostgresService,
    ):
        self.model_schema_class = model_schema_class
        self.postgres_service = postgres_service

    async def create_model(self, model_schema: UserCreate) -> UserModel:
        try:
            db_model: UserModel = await self.postgres_service.create(model_schema)
        except IntegrityError:
            raise InvalidFieldException
        return db_model

    async def get_model_by_id(self, model_id: UUID) -> UserModel:

        db_model: UserModel = await self.postgres_service.get_by_id(model_id)

        if not db_model:
            return None

        return db_model

    async def get_all_models(self) -> Sequence[UserModel]:

        db_models: Sequence[UserModel] = await self.postgres_service.get_all()

        return db_models


def get_user_service(
    pg_session: AsyncSession = Depends(get_session),
) -> UserService:
    return UserService(
        model_schema_class=UserSchema,
        postgres_service=PostgresService(
            session=pg_session, model_class=UserModel
        ),
    )
