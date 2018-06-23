import os

from mongomock import MongoClient
from umongo import Instance


def setup_db(mongo_client=MongoClient,):
    connection_string = os.environ.get('USER_MODULE_DB','')
    db_name = os.environ.get('USER_MODULE_DB_NAME','')

    mongo_client = mongo_client(connection_string, connect=True, maxPoolSize=200, connectTimeoutMS=120000,
                                socketTimeoutMS=120000)
    db = mongo_client[db_name]
    db_umongo_instance = Instance(db)

    return db, db_umongo_instance


db, db_instance = setup_db()
