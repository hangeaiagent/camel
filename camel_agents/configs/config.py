"""
CAMEL智能体配置
"""
from pydantic_settings import BaseSettings
from typing import Optional, Dict, Any
import os


class AgentConfig(BaseSettings):
    """智能体配置类"""
    
    # AI模型配置
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    
    # 默认模型设置
    conversation_model: str = "gpt-4o-mini"
    planning_model: str = "gpt-4o-mini"
    route_model: str = "gpt-4o-mini"
    
    # 模型参数
    temperature: float = 0.7
    max_tokens: int = 2048
    
    # 工具包配置
    enable_search: bool = True
    enable_maps: bool = True
    enable_translation: bool = True
    
    # 缓存配置
    enable_memory: bool = True
    memory_cache_size: int = 1000
    
    # 调试模式
    debug_mode: bool = False
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        env_prefix = "CAMEL_"


# 创建全局配置实例
agent_config = AgentConfig()

# 智能体角色配置
AGENT_ROLES = {
    "conversation_agent": {
        "role_name": "Travel Conversation Assistant",
        "description": "专业的旅行对话助手，负责理解用户需求和意图识别",
        "system_message": """你是一个专业的旅行规划助手。你的任务是：
1. 理解用户的旅行需求和意图
2. 提取关键信息（目的地、时间、预算、偏好等）
3. 提供友好和专业的对话体验
4. 支持中文和英文交流

请始终保持热情和专业，为用户提供有价值的旅行建议。"""
    },
    
    "planning_agent": {
        "role_name": "Travel Planning Specialist",
        "description": "专业的旅行规划专家，负责制定详细的旅行计划",
        "system_message": """你是一个专业的旅行规划专家。你的任务是：
1. 根据用户需求制定详细的旅行计划
2. 提供合理的预算估算和分解
3. 推荐适合的景点、住宿和餐饮
4. 考虑当地文化、天气和最佳旅行时间

请确保计划的可行性和实用性。"""
    },
    
    "route_agent": {
        "role_name": "Route Optimization Expert",
        "description": "路线优化专家，负责交通路线规划和优化",
        "system_message": """你是一个路线优化专家。你的任务是：
1. 规划最优的交通路线和时间安排
2. 比较不同交通方式的优缺点
3. 考虑成本、时间和舒适度的平衡
4. 提供实用的交通建议和注意事项

请优先考虑用户的偏好和预算限制。"""
    }
}

# 工具包配置
TOOLKIT_CONFIG = {
    "search_toolkit": {
        "enabled": True,
        "apis": ["duckduckgo", "wikipedia"],
        "language": "zh-cn"
    },
    
    "translation_toolkit": {
        "enabled": True,
        "supported_languages": ["zh-CN", "en-US", "ja-JP", "ko-KR"],
        "default_target": "zh-CN"
    },
    
    "memory_toolkit": {
        "enabled": True,
        "max_context_length": 4000,
        "memory_types": ["conversation", "user_preferences", "travel_history"]
    },
    
    "math_toolkit": {
        "enabled": True,
        "optimization_algorithms": ["dijkstra", "genetic", "simulated_annealing"]
    }
}
