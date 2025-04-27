from pymongo import ASCENDING, DESCENDING
from common.connection import MongoDBConnectionManager
from common.server import mcp  # 修改导入路径

@mcp.tool()
async def create_index(collection: str, field: str, order: str = "asc") -> dict:
    """创建索引
    
    Args:
        collection: 集合名称
        field: 字段名称
        order: 排序方式(asc/desc)
        
    Returns:
        创建结果
    """
    try:
        db = MongoDBConnectionManager.get_database()
        direction = ASCENDING if order == "asc" else DESCENDING
        result = db[collection].create_index([(field, direction)])
        return {
            "status": "success",
            "index_name": result
        }
    except Exception as e:
        return {"error": str(e)}