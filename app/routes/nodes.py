from typing import List
from uuid import uuid4
from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from app.db.database_manager import DatabaseManager

from app.db.models import VirtualNode
from app.db import db, get_database


router = APIRouter(prefix="/nodes", tags=["Nodes"])


@router.get("/")
async def all_nodes(db: DatabaseManager = Depends(get_database)):
    nodes = await db.get_virtual_nodes()
    return list(nodes)


@router.post("/", response_description="Add new virtual node", response_model=VirtualNode)
async def create_virtual_node(node: VirtualNode = Body(...)):
    node = jsonable_encoder(node)
    new_node = await db["virtual_nodes"].insert_one(node)
