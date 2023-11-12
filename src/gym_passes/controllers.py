from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from kink import di

from src.building_blocks.errors import APIErrorMessage
from src.gym_passes.application.dto import CreateGymPassDTO, GymPassDTO, PauseGymPassDTO
from src.gym_passes.application.gym_pass_service import GymPassService

router = APIRouter()


@router.post(
    "/gym-passes",
    response_model=GymPassDTO,
    responses={400: {"model": APIErrorMessage}, 500: {"model": APIErrorMessage}},
    tags=["gym_passes"],
)
async def create_gym_pass(
    request: CreateGymPassDTO, service: GymPassService = Depends(lambda: di[GymPassService])
) -> JSONResponse:
    result = service.create(request)
    return JSONResponse(content=result.dict(), status_code=status.HTTP_201_CREATED)
