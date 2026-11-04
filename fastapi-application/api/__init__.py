from fastapi import APIRouter

from core.config import settings
from .api_v1 import router as router_api_v1

router = APIRouter(
    prefix=settings.api.v1.prefix,   # "/v1"
)
router.include_router(router_api_v1)