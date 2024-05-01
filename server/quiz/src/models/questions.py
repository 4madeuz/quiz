import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, JSON, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from src.db.postgres import Base
from src.models.mixins import IdMixin, TimestampMixin


class Result(Base, IdMixin, TimestampMixin):
    __tablename__ = "results"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    survey_id = Column(UUID(as_uuid=True), ForeignKey("surveys.id"), primary_key=True)
    correct_answers = Column(ARRAY(UUID(as_uuid=True)))
    survey_len = Column(Integer)
    answers_amount = Column(Integer)
    survey = relationship("Survey", back_populates="results", lazy="selectin")
    user = relationship("User", back_populates="results", lazy="selectin")


class Survey(Base, IdMixin, TimestampMixin):
    __tablename__ = "surveys"

    title = Column(String)
    questions = relationship("Question", back_populates="survey", cascade="all, delete", passive_deletes=True, lazy="selectin")
    users = relationship("User", secondary=Result.__table__, back_populates="surveys", lazy="selectin")
    survey_json = Column(JSON)
    published = Column(Boolean, default=False)
    results = relationship("Result", cascade="all, delete", passive_deletes=True, lazy="selectin")


class Question(Base, IdMixin, TimestampMixin):
    __tablename__ = "questions"

    name = Column(String)
    title = Column(String)
    recommendation = Column(String)
    survey_id = Column(UUID(as_uuid=True), ForeignKey("surveys.id", ondelete="CASCADE"))
    survey = relationship("Survey", back_populates="questions")
    options = Column(ARRAY(String))
    answers = Column(String)
