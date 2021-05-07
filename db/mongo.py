from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient


async def connect_to_db(app: FastAPI) -> None:
    app.state.db_client = AsyncIOMotorClient()


async def close_db_connection(app: FastAPI) -> None:
    app.state.db_client.close()
