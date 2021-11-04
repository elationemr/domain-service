from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()


@router.get(
    "/status",
    description="Get API status."
)
def get_status():
    return PlainTextResponse(status_code=200, content="OK")

@router.get(
    "/domain-service",
    description="Get root."
)
def get_status():
    return PlainTextResponse(status_code=200, content="BEN WUZ HERE")
