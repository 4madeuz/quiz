from fastapi import APIRouter, Depends, HTTPException

from typing import List
from uuid import UUID
from src.schemas.users import UserCreate, User, UserShort
from src.services.user_service import UserService, get_user_service

router = APIRouter()


@router.post("/", response_model=UserShort)
async def create_user(user_data: UserCreate, service: UserService = Depends(get_user_service)):
    return await service.create_model(user_data)


@router.get("/{user_id}", response_model=User)
async def read_user(user_id: UUID, service: UserService = Depends(get_user_service)):
    user = await service.get_model_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=list[User])
async def read_all_users(service: UserService = Depends(get_user_service)):
    users = await service.get_all_models()
    return users
