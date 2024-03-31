from fastapi import APIRouter

from api.v1.endpoints import main, oauth

api_router = APIRouter()
api_router.include_router(main.router, prefix="/main", tags=["main"])
api_router.include_router(oauth.router, prefix="/oauth", tags=["oauth"])
