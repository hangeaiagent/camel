"""
Travel AI Backend - Main FastAPI Application
"""
from fastapi import FastAPI, WebSocket, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
import uvicorn
import logging
from datetime import datetime
from typing import Dict, Any

from .core.config import settings
from .api import auth, chat, users
from .db.database import engine, Base

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建FastAPI应用
app = FastAPI(
    title="Travel AI API",
    description="对话式AI旅游规划引擎API",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json"
)

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 安全配置
security = HTTPBearer()

# 创建数据库表
@app.on_event("startup")
async def startup_event():
    """应用启动时创建数据库表"""
    # Base.metadata.create_all(bind=engine)
    logger.info("Travel AI Backend started successfully")

# 包含路由
app.include_router(auth.router, prefix="/api/v1/auth", tags=["认证"])
app.include_router(chat.router, prefix="/api/v1/chat", tags=["对话"])
app.include_router(users.router, prefix="/api/v1/users", tags=["用户"])

@app.get("/")
async def root():
    """根路径健康检查"""
    return {
        "message": "Travel AI Backend API",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """健康检查端点"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    """WebSocket连接处理对话"""
    await websocket.accept()
    logger.info(f"WebSocket connection established for user: {user_id}")
    
    try:
        while True:
            # 接收用户消息
            user_message = await websocket.receive_text()
            logger.info(f"Received message from {user_id}: {user_message}")
            
            # TODO: 集成CAMEL智能体处理消息
            # 暂时返回模拟响应
            response = {
                "type": "response",
                "content": {
                    "text": f"收到您的消息: {user_message}. 这是一个模拟响应，AI智能体功能正在开发中。",
                    "intent": "general_query",
                    "entities": {},
                },
                "timestamp": datetime.now().isoformat(),
                "user_id": user_id
            }
            
            # 发送响应
            await websocket.send_json(response)
            
    except Exception as e:
        logger.error(f"WebSocket error for user {user_id}: {str(e)}")
        await websocket.send_json({
            "type": "error",
            "message": f"连接错误: {str(e)}",
            "timestamp": datetime.now().isoformat()
        })
    finally:
        logger.info(f"WebSocket connection closed for user: {user_id}")

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
