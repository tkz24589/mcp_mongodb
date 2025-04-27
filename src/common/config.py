"""
MongoDB 连接配置模块
从环境变量加载配置并生成 MongoDB 连接 URI
"""

import urllib
from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()

# MCP 传输协议配置，默认为 stdio
MCP_TRANSPORT = os.getenv('MCP_TRANSPORT', 'sse')

# MongoDB 连接配置字典
MONGO_CFG = {
    "host": os.getenv('MONGO_HOST', 'localhost'),  # MongoDB 服务器地址
    "port": int(os.getenv('MONGO_PORT', 27017)),  # MongoDB 端口号
    "username": os.getenv('MONGO_USERNAME', None),  # MongoDB 用户名(可选)
    "password": os.getenv('MONGO_PWD', ''),        # MongoDB 密码
    "auth_source": os.getenv('MONGO_AUTH_SOURCE', None),  # 认证数据库
    "replica_set": os.getenv('MONGO_REPLICA_SET', None),     # 副本集名称
    "ssl": os.getenv('MONGO_SSL', False) in ('true', '1', 't'),  # 是否启用 SSL
    "tls": os.getenv('MONGO_TLS', False) in ('true', '1', 't'),  # 是否启用 TLS
    "tls_ca_file": os.getenv('MONGO_TLS_CA_FILE', None),      # CA 证书文件路径
    "tls_certificate_key_file": os.getenv('MONGO_TLS_CERT_KEY_FILE', None),  # 证书密钥文件
    "direct_connection": os.getenv('MONGO_DIRECT_CONNECTION', False) in ('true', '1', 't')  # 是否直接连接
}

def generate_mongo_uri():
    """
    生成 MongoDB 连接 URI
    根据配置生成带认证信息和 SSL/TLS 参数的连接字符串
    
    返回:
        str: 完整的 MongoDB 连接 URI
    """
    cfg = MONGO_CFG
    # 使用 mongodb+srv 需要去掉端口号
    scheme = "mongodb+srv" if cfg.get("ssl") else "mongodb"
    host = cfg.get("host", "localhost")
    port = cfg.get("port", 27017)
    
    # 认证信息处理
    auth_part = ""
    if cfg.get("username"):
        auth_part = f"{urllib.parse.quote(cfg['username'])}:{urllib.parse.quote(cfg['password'])}@"
    elif cfg.get("password"):
        auth_part = f":{urllib.parse.quote(cfg['password'])}@"
    
    # 基础 URI 构建
    base_uri = f"{scheme}://{auth_part}{host}"
    # mongodb+srv 协议不能指定端口
    if scheme == "mongodb":
        base_uri += f":{port}/"
    
    # 查询参数处理
    query_params = {}
    # 必须参数
    if cfg.get("auth_source"):
        query_params["authSource"] = cfg["auth_source"]
    
    # 副本集参数
    if cfg.get("replica_set"):
        query_params["replicaSet"] = cfg["replica_set"]
    
    # TLS/SSL 参数
    if cfg.get("ssl"):
        query_params["ssl"] = "true"
    if cfg.get("tls"):
        query_params["tls"] = "true"
    if cfg.get("tls_ca_file"):
        query_params["tlsCAFile"] = cfg["tls_ca_file"]
    if cfg.get("tls_certificate_key_file"):
        query_params["tlsCertificateKeyFile"] = cfg["tls_certificate_key_file"]
    
    # 连接方式
    if cfg.get("direct_connection"):
        query_params["directConnection"] = "true"
    
    # 添加查询参数到 URI
    if query_params:
        base_uri += "/?" + urllib.parse.urlencode(query_params)
    
    return base_uri

def get_mongo_client_kwargs():
    """
    获取 MongoClient 初始化参数，排除已在 URI 中包含的参数
    """
    cfg = MONGO_CFG.copy()
    # 移除已在 URI 中处理的参数
    for key in ['host', 'port', 'username', 'password', 'auth_source', 
               'replica_set', 'ssl', 'tls', 'tls_ca_file', 
               'tls_certificate_key_file', 'direct_connection']:
        cfg.pop(key, None)
    return cfg