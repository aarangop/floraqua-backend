import logging
from typing import List, Union

from bson import ObjectId
from fastapi import Body
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.db.database_manager import DatabaseManager
from app.db.models import VirtualNode, PyObjectId


class MongoManager(DatabaseManager):
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None
    db_name: str = None

    async def connect_to_database(
        self,
        db_path: str,
        db_name: str
    ):
        self.db_name = db_name
        self.client = AsyncIOMotorClient(
            db_path,
            maxPoolSize=10,
            minPoolSize=10)
        self.db = self.client[db_name]

    async def close_database_connection(self):
        self.client.close()

    async def get_virtual_nodes(self) -> List[VirtualNode]:
        nodes_list = []
        nodes_q = self.db.virtual_nodes.find()

        async for node in nodes_q:
            nodes_list.append(VirtualNode(**node, id=node['_id']))
        return nodes_list

    async def add_node(self, node: VirtualNode) -> Union[ObjectId, None]:
        res = await self.db.virtual_nodes.insert_one(node)
        if res.inserted_id:
            return node
