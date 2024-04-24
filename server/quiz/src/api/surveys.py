from fastapi import APIRouter, Depends, HTTPException

from src.schemas.questions import SurveyCreate, Survey
from src.services.survey_service import SurveyService, get_survey_service

router = APIRouter()


@router.post("/", response_model=Survey)
async def create_survey(survey_data: SurveyCreate, service: SurveyService = Depends(get_survey_service)):
    return await service.create_model(survey_data)


@router.get("/{survey_id}", response_model=Survey)
async def read_survey(survey_id: str, service: SurveyService = Depends(get_survey_service)):
    survey = await service.get_model_by_id(survey_id)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey


@router.get("/", response_model=list[Survey])
async def read_all_surveys(service: SurveyService = Depends(get_survey_service)):
    return await service.get_all_models()
