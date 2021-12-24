from fastapi import APIRouter, Depends
from starlette.requests import Request

from custom_server.core import settings

from custom_server.core.schemas import HearbeatResult, LoanModelPayload, LoanPredictionResult

router = APIRouter()
inference_router = APIRouter()

@router.get("heartbeat", response_model=HearbeatResult, name='heartbeat')
def get_heartbeat():
    heartbeat = HearbeatResult(is_alive=True)
    return heartbeat


@inference_router.post("/predict", response_model=LoanPredictionResult, name="predict")
def post_predict(
    request: Request,
    authenticated: bool = Depends(settings.validate_request),
    loan_data: LoanModelPayload = None
) -> LoanPredictionResult:

    model = request.app.state.model
    prediction = model.predict(loan_data)

    return prediction