from fastapi import APIRouter, Depends, HTTPException

from src.schemas.questions import SurveyCreate, Survey, ResultCreate
from src.services.survey_service import SurveyService, get_survey_service
from src.schemas.users import User
from src.services.token import get_current_user

router = APIRouter()


@router.post("/", response_model=Survey)
async def create_survey(survey_data: SurveyCreate, service: SurveyService = Depends(get_survey_service)):
    return await service.create_survey(survey_data)


@router.get("/{survey_id}", response_model=Survey)
async def read_survey(survey_id: str, service: SurveyService = Depends(get_survey_service)):
    survey = await service.get_model_by_id(survey_id)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey


@router.get("/", response_model=list[Survey])
async def read_all_surveys(
    service: SurveyService = Depends(get_survey_service),
    current_user: User = Depends(get_current_user)
     ):
    return await service.get_all_models(current_user)


@router.delete("/{survey_id}")
async def delete_survey(survey_id: str, service: SurveyService = Depends(get_survey_service)):
    return await service.delete_survey(survey_id)


@router.post("/publish/{survey_id}", response_model=Survey)
async def publish_survey(survey_id: str, service: SurveyService = Depends(get_survey_service)):
    return await service.publish_survey(survey_id)
