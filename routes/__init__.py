from fastapi import APIRouter
from routes.gists import router as chat_router

router = APIRouter()

router.include_router(chat_router, prefix="/gists")
