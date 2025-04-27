from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from .config import MONGO_CFG, generate_mongo_uri, get_mongo_client_kwargs

class MongoDBConnectionManager:
    _client = None
    _database = None
    
    @classmethod
    def initialize(cls, uri: str = None, db_name: str = None):
        """初始化 MongoDB 连接"""
        uri = generate_mongo_uri()
        client_kwargs = get_mongo_client_kwargs()
        db_name = db_name or os.getenv("MONGO_DB", "mcp_db")
        print("MongoDB URI:", uri)  # 调试用，打印 URI
        print("MongoDB Client kwargs:", client_kwargs)  # 调试用，打印 client kwargs
        print("MongoDB Database name:", db_name)  # 调试用，打印数据库名
        try:
            cls._client = MongoClient(uri, **client_kwargs)
            cls._client.admin.command('ping')  # 主动验证连接
            cls._database = cls._client[db_name]
        except ConnectionFailure as e:
            print(f"Connection failed: {e}")
            cls._database = None
        except Exception as e:
            print(f"Unexpected error: {e}")
            cls._database = None
    
    @classmethod
    def get_database(cls):
        """获取数据库实例"""
        try:
            cls._client.admin.command('ping')
        except:
            cls.initialize()
        return cls._database
    
    @classmethod
    def close(cls):
        """关闭连接"""
        if cls._client:
            cls._client.close()