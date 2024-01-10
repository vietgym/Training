from fastapi import APIRouter

from app.api import endpoint

router = APIRouter()

router.include_router(endpoint.route, tags=["users"])