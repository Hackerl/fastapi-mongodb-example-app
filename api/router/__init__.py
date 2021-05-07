from fastapi import APIRouter

from api.router import machine

router = APIRouter()

router.include_router(machine.router)
