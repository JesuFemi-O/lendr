from starlette.config import Config
from starlette.datastructures import Secret
import secrets
from typing import Optional

from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

from custom_server.core.messages import AUTH_REQ, NO_API_KEY

APP_VERSION = "0.0.1"
APP_NAME = "Loan Eligiblity Prediction"
API_PREFIX = "/api"

config = Config(".env")

API_KEY: Secret = config("API_KEY", cast=Secret)
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)

DEFAULT_MODEL_PATH: str = config("DEFAULT_MODEL_PATH")

api_key = APIKeyHeader(name="token", auto_error=False)


def validate_request(header: Optional[str] = Security(api_key)) -> bool:
    if header is None:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=NO_API_KEY, headers={}
        )
    if not secrets.compare_digest(header, str(API_KEY)):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED, detail=AUTH_REQ, headers={}
        )
    return True