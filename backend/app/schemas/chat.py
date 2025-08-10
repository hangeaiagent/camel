"""
对话相关数据模型
"""
from pydantic import BaseModel
from typing import Dict, List, Any, Optional
from datetime import datetime


class ChatMessage(BaseModel):
    """对话消息"""
    content: str
    user_id: str
    conversation_id: Optional[str] = None
    message_type: str = "text"


class ChatResponse(BaseModel):
    """对话响应"""
    response_id: str
    content: str
    intent: str
    entities: Dict[str, Any]
    suggestions: List[str] = []
    timestamp: datetime
    
    class Config:
        from_attributes = True


class Conversation(BaseModel):
    """对话会话"""
    conversation_id: str
    user_id: str
    title: str
    status: str = "active"
    created_at: datetime
    updated_at: datetime
    message_count: int = 0
    
    class Config:
        from_attributes = True


class TravelPlan(BaseModel):
    """旅行计划"""
    plan_id: str
    user_id: str
    title: str
    destination: str
    duration: str
    budget: str
    plan_data: Dict[str, Any]
    status: str = "draft"
    created_at: datetime
    
    class Config:
        from_attributes = True
