import logging
from typing import List

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.db.database_manager import DatabaseManager
from app.db.models import VirtualNode, PyObjectId


class MongoManager(DatabaseManager):
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None
    db_name: str = None

    async def connect_to_database(self, path: str, db_name: str):
        logging.info("Connecting to MongoDB.")
        self.db_name = db_name
        self.client = AsyncIOMotorClient(
            path,
            maxPoolSize=10,
            minPoolSize=10)
        self.db = self.client[db_name]
        logging.info("Connected to MongoDB.")

    async def close_database_connection(self):
        logging.info("Closing connection with MongoDB.")
        self.client.close()
        logging.info("Closed connection with MongoDB.")

    async def get_virtual_nodes(self) -> List[VirtualNode]:
        nodes_list = []
        nodes_q = self.db.nodes.find()

        async for node in nodes_q:
            nodes_list.append(VirtualNode(**node, id=node['_id']))
        return nodes_list

    # async def get_posts(self) -> List[PostDB]:
    #     posts_list = []
    #     posts_q = self.db.posts.find()
    #     async for post in posts_q:
    #         posts_list.append(PostDB(**post, id=post['_id']))
    #     return posts_list

    # async def get_post(self, post_id: OID) -> PostDB:
    #     post_q = await self.db.posts.find_one({'_id': ObjectId(post_id)})
    #     if post_q:
    #         return PostDB(**post_q, id=post_q['_id'])

    # async def delete_post(self, post_id: OID):
    #     await self.db.posts.delete_one({'_id': ObjectId(post_id)})

    # async def update_post(self, post_id: OID, post: PostDB):
    #     await self.db.posts.update_one({'_id': ObjectId(post_id)},
    #                                    {'$set': post.dict(exclude={'id'})})

    # async def add_post(self, post: PostDB):
    #     await self.db.posts.insert_one(post.dict(exclude={'id'}))