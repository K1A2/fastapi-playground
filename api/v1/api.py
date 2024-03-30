from fastapi import APIRouter

from api.v1.endpoints import main

api_router = APIRouter()
api_router.include_router(main.router, prefix="/main", tags=["main"])
