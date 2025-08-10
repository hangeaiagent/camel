"""
认证相关数据模型
"""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserLogin(BaseModel):
    """用户登录请求"""
    username: str
    password: str


class UserRegister(BaseModel):
    """用户注册请求"""
    username: str
    email: EmailStr
    password: str
    confirm_password: str


class Token(BaseModel):
    """JWT令牌响应"""
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    user_id: str


class User(BaseModel):
    """用户信息"""
    user_id: str
    username: str
    email: str
    created_at: datetime
    is_active: bool = True
    
    class Config:
        from_attributes = True
