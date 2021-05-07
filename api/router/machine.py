from bson import ObjectId
from fastapi import APIRouter, Depends

from api.dependencies.database import get_collection
from core.config import MACHINE_COLLECTION
from model.machine import Machine
from model.response import Response, Page
from service.paginate import MongoDBPage

router = APIRouter()


@router.post("/machines", response_model=Response[Machine])
async def create_machine(machine: Machine, collection=Depends(get_collection(MACHINE_COLLECTION))):
    result = await collection.insert_one(machine.dict(by_alias=True))
    machine.id = result.inserted_id
    return Response[Machine](data=machine)


@router.get("/machines", response_model=Response[Page[Machine]])
async def get_machines(page: int = 1, page_size: int = 30, collection=Depends(get_collection(MACHINE_COLLECTION))):
    page = await MongoDBPage(collection, Machine).paginate(page=page, page_size=page_size)
    return Response[Page[Machine]](data=page)


@router.get("/machine/{machine_id}", response_model=Response[Machine])
async def get_machine(machine_id: str, collection=Depends(get_collection(MACHINE_COLLECTION))):
    result = await collection.find_one(filter=ObjectId(machine_id))
    return Response[Machine](data=Machine(**result))
