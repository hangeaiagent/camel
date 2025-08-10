"""
应用配置设置
"""
from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    """应用配置类"""
    
    # 基础配置
    app_name: str = "Travel AI Backend"
    debug: bool = False
    version: str = "1.0.0"
    
    # 数据库配置
    database_url: str = "postgresql://dev_user:dev_password@localhost:5432/travel_ai_dev"
    
    # Redis配置
    redis_url: str = "redis://localhost:6379"
    
    # JWT配置
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 1440  # 24小时
    
    # AI模型配置
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    
    # 向量数据库配置
    qdrant_url: str = "http://localhost:6333"
    qdrant_api_key: Optional[str] = None
    
    # CORS配置
    allowed_origins: list = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# 创建配置实例
settings = Settings()
