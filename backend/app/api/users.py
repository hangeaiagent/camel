"""
用户管理相关API
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Dict, Any, List
from datetime import datetime

router = APIRouter()
security = HTTPBearer()

@router.get("/profile")
async def get_user_profile(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """获取用户个人资料"""
    # TODO: 从数据库获取真实用户资料
    return {
        "user_id": "demo-user-123",
        "username": "demo",
        "email": "demo@example.com",
        "preferences": {
            "preferred_languages": ["zh-CN", "en-US"],
            "travel_style": "文化探索",
            "budget_range": "中等",
            "favorite_destinations": ["日本", "欧洲"]
        },
        "stats": {
            "total_conversations": 15,
            "travel_plans_created": 5,
            "last_active": datetime.now().isoformat()
        }
    }

@router.put("/preferences")
async def update_user_preferences(
    preferences: Dict[str, Any],
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """更新用户偏好设置"""
    # TODO: 保存到数据库
    return {
        "message": "用户偏好更新成功",
        "preferences": preferences,
        "updated_at": datetime.now().isoformat()
    }

@router.get("/travel-plans")
async def get_user_travel_plans(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """获取用户的旅行计划"""
    # TODO: 从数据库获取真实数据
    mock_plans = [
        {
            "plan_id": "plan_1",
            "title": "日本东京5日游",
            "destination": "日本",
            "duration": "5天",
            "budget": "10000元",
            "status": "已完成",
            "created_at": "2025-07-15T10:00:00",
            "summary": "东京深度游，包含浅草寺、银座、新宿等热门景点"
        },
        {
            "plan_id": "plan_2",
            "title": "欧洲三国10日游",
            "destination": "欧洲",
            "duration": "10天", 
            "budget": "25000元",
            "status": "草稿",
            "created_at": "2025-08-01T14:30:00",
            "summary": "法国-意大利-德国经典路线"
        }
    ]
    
    return {
        "travel_plans": mock_plans,
        "total_count": len(mock_plans)
    }
