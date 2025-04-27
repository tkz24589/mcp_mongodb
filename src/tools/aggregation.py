from common.connection import MongoDBConnectionManager
from common.server import mcp

@mcp.tool()  # 修改为 @mcp.tool()
async def aggregate(collection: str, pipeline: list) -> list:
    """执行聚合操作
    
    Args:
        collection: 集合名称
        pipeline: 聚合管道
        
    Returns:
        聚合结果
    """
    try:
        db = MongoDBConnectionManager.get_database()
        return list(db[collection].aggregate(pipeline))
    except Exception as e:
        return {"error": str(e)}