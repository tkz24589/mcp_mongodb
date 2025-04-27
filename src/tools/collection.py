from common.connection import MongoDBConnectionManager
from common.server import mcp

@mcp.tool()  # 修改为 @mcp.tool()
async def create_collection(name: str, **options) -> dict:
    """创建新集合
    
    Args:
        name: 集合名称
        options: 集合选项
        
    Returns:
        创建结果
    """
    try:
        db = MongoDBConnectionManager.get_database()
        db.create_collection(name, **options)
        return {"status": "success", "message": f"Collection '{name}' created"}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()  # 修改为 @mcp.tool()
async def list_collections() -> list:
    """列出所有集合
    
    Returns:
        集合名称列表
    """
    try:
        db = MongoDBConnectionManager.get_database()
        return [col["name"] for col in db.list_collections()]
    except Exception as e:
        return {"error": str(e)}