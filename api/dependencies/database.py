from typing import Callable

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.requests import Request

from core.config import DATABASE


def _get_db_client(request: Request) -> AsyncIOMotorClient:
    return request.app.state.db_client


def get_collection(collection: str) -> Callable:
    def _get_collection(client: AsyncIOMotorClient = Depends(_get_db_client)):
        return client[DATABASE][collection]

    return _get_collection
