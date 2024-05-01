import uuid

from sqlalchemy import Column, String, Boolean
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship

from src.models.mixins import IdMixin, TimestampMixin
from src.models.questions import Result
from src.db.postgres import Base


class User(Base, IdMixin, TimestampMixin):
    __tablename__ = "users"

    username = Column(String, unique=True)
    email = Column(EmailType, unique=True)
    is_admin = Column(Boolean, default=False)
    surveys = relationship("Survey", secondary=Result.__table__, back_populates="users", lazy="selectin")
    results = relationship("Result", cascade="all, delete", passive_deletes=True, lazy="selectin")
    password = Column(String)
