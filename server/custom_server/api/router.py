from fastapi import APIRouter

from custom_server.api import views

api_router = APIRouter()
api_router.include_router(views.router, tags=["health"], prefix="/health")
api_router.include_router(views.inference_router, tags=[
                          "prediction"], prefix="/model")