import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.db.postgres import Base
from src.models.mixins import IdMixin, TimestampMixin

user_survey_association = Table(
    "user_survey_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("survey_id", Integer, ForeignKey("surveys.id")),
)


class Survey(IdMixin, TimestampMixin):
    __tablename__ = "surveys"

    title = Column(String)
    questions = relationship("Question", back_populates="survey")
    users = relationship("User", secondary=user_survey_association, back_populates="surveys")


class Question(IdMixin, TimestampMixin):
    __tablename__ = "questions"

    text = Column(String)
    survey_id = Column(UUID(as_uuid=True), ForeignKey("surveys.id"), default=uuid.uuid4)
    survey = relationship("Survey", back_populates="questions")
    options = relationship("Option", back_populates="question")


class Option(IdMixin, TimestampMixin):
    __tablename__ = "options"

    text = Column(String)
    is_correct = Column(Integer)
    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id"), default=uuid.uuid4)
    question = relationship("Question", back_populates="options")
