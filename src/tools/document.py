from common.connection import MongoDBConnectionManager
from common.server import mcp

@mcp.tool()  # 修改为 @mcp.tool()
async def insert_one(collection: str, document: dict) -> dict:
    """插入单个文档到MongoDB集合
    
    Args:
        collection: 集合名称
        document: 要插入的文档(dict)
        
    Returns:
        插入结果和文档ID
    """
    try:
        db = MongoDBConnectionManager.get_database()
        result = db[collection].insert_one(document)
        return {
            "status": "success",
            "inserted_id": str(result.inserted_id)
        }
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()  # 修改为 @mcp.tool()
async def find_one(collection: str, query: dict = None) -> dict:
    """查询单个文档
    
    Args:
        collection: 集合名称
        query: 查询条件(dict)
        
    Returns:
        找到的文档或None
    """
    try:
        db = MongoDBConnectionManager.get_database()
        result = db[collection].find_one(query or {})
        print(f"{collection} Query result: {result}")  # 调试输出查询结果
        return result
    except Exception as e:
        return {"error": f"Query execution failed: {str(e)}"}