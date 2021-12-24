from fastapi import FastAPI
from loguru import logger
from typing import Callable

from custom_server.core.settings import DEFAULT_MODEL_PATH
from custom_server.services.loans import LoanService


def _startup_model(app: FastAPI) -> None:
    model_path = DEFAULT_MODEL_PATH
    model_instance = LoanService(model_path)
    app.state.model = model_instance
    logger.info("Model Loaded into memory...")


def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("Running app start handler.")
        _startup_model(app)
    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Running app shutdown handler.")
        _shutdown_model(app)
    return shutdown