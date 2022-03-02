from abc import abstractmethod
from typing import List

from app.db.models import VirtualNode


class DatabaseManager(object):
    @property
    def client(self):
        raise NotImplementedError

    @property
    def db(self):
        raise NotImplementedError

    @abstractmethod
    async def connect_to_database(
            self,
            db_path: str,
            db_name: str):
        pass

    @abstractmethod
    async def close_database_connection(self):
        pass

    @abstractmethod
    async def get_virtual_nodes(self) -> List[VirtualNode]:
        pass

    @abstractmethod
    async def add_node(self, node: VirtualNode):
        pass

        # @abstractmethod
        # async def get_post(self, post_id: OID) -> PostDB:
        #     pass

        # @abstractmethod
        # async def add_post(self, post: PostDB):
        #     pass

        # @abstractmethod
        # async def update_post(self, post_id: OID, post: PostDB):
        #     pass

        # @abstractmethod
        # async def delete_post(self, post_id: OID):
        #     pass
