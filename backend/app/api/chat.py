"""
对话相关API
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Dict, Any, List
from datetime import datetime

from ..schemas.chat import ChatMessage, ChatResponse

router = APIRouter()
security = HTTPBearer()

@router.post("/send", response_model=ChatResponse)
async def send_message(
    message: ChatMessage,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """发送对话消息"""
    # TODO: 集成CAMEL智能体处理消息
    # 暂时返回模拟响应
    
    response_text = f"收到您的消息: {message.content}. 这是一个模拟响应。"
    
    if "旅游" in message.content or "旅行" in message.content:
        response_text = "我是您的旅行规划助手！请告诉我您想去哪里，计划多长时间的旅行，以及您的预算范围，我会为您制定详细的旅行计划。"
    elif "推荐" in message.content:
        response_text = "根据您的需求，我推荐以下几个目的地：\n1. 日本 - 文化体验丰富\n2. 泰国 - 性价比高\n3. 欧洲 - 历史悠久\n请告诉我您更偏好哪种类型的旅行？"
    
    return ChatResponse(
        response_id=f"resp_{datetime.now().timestamp()}",
        content=response_text,
        intent="travel_planning",
        entities={},
        suggestions=["我想去日本旅游", "推荐欧洲路线", "制定预算计划"],
        timestamp=datetime.now()
    )

@router.get("/history/{user_id}")
async def get_chat_history(
    user_id: str,
    limit: int = 20,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """获取用户对话历史"""
    # TODO: 从数据库获取真实的对话历史
    mock_history = [
        {
            "message_id": "msg_1",
            "content": "我想去日本旅游5天",
            "response": "好的！日本5天游是很不错的选择。请告诉我您的预算和偏好的城市？",
            "timestamp": datetime.now().isoformat(),
            "intent": "travel_planning"
        },
        {
            "message_id": "msg_2", 
            "content": "预算1万元，想去东京和大阪",
            "response": "为您推荐东京-大阪5日游路线：\n第1-3天：东京（浅草寺、银座、新宿）\n第4-5天：大阪（大阪城、道顿堀、环球影城）",
            "timestamp": datetime.now().isoformat(),
            "intent": "route_planning"
        }
    ]
    
    return {
        "user_id": user_id,
        "messages": mock_history[:limit],
        "total_count": len(mock_history)
    }
