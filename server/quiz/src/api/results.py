from fastapi import APIRouter, Depends, HTTPException

from src.schemas.questions import SurveyCreate, Survey, ResultCreate, Result, RecomendationView, ResultDetail
from src.services.results_service import ResultService, get_result_service
from src.schemas.users import User
from src.services.token import get_current_user

router = APIRouter()


@router.get("/{result_id}", response_model=RecomendationView)
async def read_result(result_id: str, service: ResultService = Depends(get_result_service)):
    result = await service.get_model_by_id(result_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Result not found")
    return result


@router.get("/", response_model=list[ResultDetail])
async def read_all_results(service: ResultService = Depends(get_result_service)):
    return await service.get_all_models()


@router.post("/",)
async def validate_results(
    result: ResultCreate,
    service: ResultService = Depends(get_result_service),
    current_user: User = Depends(get_current_user)
        ):
    return await service.validate_results(result, current_user)


@router.get("/user/{user_id}", response_model=list[ResultDetail])
async def get_users_results(user_id: str, service: ResultService = Depends(get_result_service)):
    results = await service.get_users_models(user_id)
    return results
