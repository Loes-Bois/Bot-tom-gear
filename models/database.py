from pymongo import MongoClient
import os_helper
from dotenv import load_dotenv
load_dotenv()


class DBClient:
    class __DBClient:
        def __init__(self):
            username = os_helper.get_env_var("DB_USERNAME")
            password = os_helper.get_env_var("DB_PASSWORD")
            db_name = os_helper.get_env_var("DB_NAME")
            
            conn_url = f"mongodb://{username}:{password}@tagstest-shard-00-00.7trbb.mongodb.net:27017,tagstest-shard-00-01.7trbb.mongodb.net:27017,tagstest-shard-00-02.7trbb.mongodb.net:27017/{db_name}?ssl=true&replicaSet=atlas-vfufs2-shard-0&authSource=admin&retryWrites=true&w=majority"
            print(conn_url)
            self.client = MongoClient(conn_url)
            self.db = self.client.Tags
            
    instance = None
    
    def __init__(self):
        if not DBClient.instance:
            DBClient.instance = DBClient.__DBClient()

    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    def get_db(self):
        return DBClient.instance.db
    def get_client(self):
        return DBClient.instance.client

