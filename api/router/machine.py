from bson import ObjectId
from fastapi import APIRouter, Depends

from api.dependencies.database import get_collection
from core.config import MACHINE_COLLECTION
from model.machine import Machine

router = APIRouter()


@router.post("/machines", response_model=Machine)
async def create_machine(machine: Machine, collection=Depends(get_collection(MACHINE_COLLECTION))):
    result = await collection.insert_one(machine.dict(by_alias=True))
    machine.id = result.inserted_id
    return machine


@router.get("/machine/{machine_id}", response_model=Machine)
async def create_machine(machine_id: str, collection=Depends(get_collection(MACHINE_COLLECTION))):
    result = await collection.find_one(filter=ObjectId(machine_id))
    return Machine(**result)
