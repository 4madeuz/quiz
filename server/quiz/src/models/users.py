import uuid

from sqlalchemy import Column, String
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship

from src.models.mixins import IdMixin, TimestampMixin
from src.models.questions import user_survey_association


class User(IdMixin, TimestampMixin):
    __tablename__ = "users"

    username = Column(String, unique=True)
    email = Column(EmailType, unique=True)
    surveys = relationship("Survey", secondary=user_survey_association, back_populates="users")
