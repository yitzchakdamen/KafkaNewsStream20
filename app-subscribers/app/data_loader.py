import os
import logging
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.cursor import Cursor
import config

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



class DataLoader:

    def client(self) -> MongoClient:
        """
        Create a MongoDB client.
        """
        client_string = f"mongodb://{config.MONGO_HOST}:{ config.MONGO_PORT}"
        client:MongoClient = MongoClient(client_string)
        return client

    def get_database(self, client: MongoClient) -> Database:
        """Create a database connection."""
        db: Database = client[config.MONGO_DATABASE]
        logger.debug("Database connection successful.")
        return db

    def get_collection(self, db: Database) -> Collection:
        """Get the specified collection from the database."""
        logger.debug(f"Fetching all records from collection: {config.MONGO_COLLECTION}")
        return db[config.MONGO_COLLECTION]

    def get_data(self ) -> list:
        """Fetch data from the database."""
        client: MongoClient = self.client()
        db: Database = self.get_database(client)
        collection: Collection = self.get_collection(db)
        result: Cursor = collection.find({},{'_id':0})
        list_result = result.to_list()
        client.close()
        return list_result

    def insert(self, message:list[dict]) -> bool:
        """Insert a new soldier into the database."""
        client: MongoClient = self.client()
        db: Database = self.get_database(client)
        collection: Collection = self.get_collection(db)
        insert = collection.insert_many(message)
        client.close()
        return insert.acknowledged
    