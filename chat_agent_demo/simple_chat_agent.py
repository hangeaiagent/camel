#!/usr/bin/env python3
"""
简单的Chat Agent示例
展示CAMEL框架的基础使用方法
"""

import os
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

def setup_environment():
    """设置环境变量"""
    # 检查API密钥
    api_keys = {
        'OPENAI_API_KEY': 'OpenAI API密钥',
        'ANTHROPIC_API_KEY': 'Anthropic API密钥',
        'GOOGLE_API_KEY': 'Google API密钥'
    }
    
    available_keys = []
    for key, desc in api_keys.items():
        if os.getenv(key):
            available_keys.append(desc)
            print(f"✅ {desc} 已配置")
        else:
            print(f"⚠️  {desc} 未配置")
    
    if not available_keys:
        print("❌ 未找到任何API密钥，请设置环境变量")
        print("示例: export OPENAI_API_KEY='your_api_key_here'")
        return False
    
    return True

def create_simple_agent():
    """创建简单的Chat Agent"""
    print("\n=== 创建简单Chat Agent ===")
    
    # 方式1: 使用默认模型
    agent = ChatAgent("你是一个有用的助手。")
    
    return agent

def create_specific_model_agent():
    """创建指定模型的Chat Agent"""
    print("\n=== 创建指定模型Chat Agent ===")
    
    # 方式2: 指定OpenAI模型
    if os.getenv('OPENAI_API_KEY'):
        agent = ChatAgent(
            "你是一个专业的AI助手，能够提供准确和有用的信息。",
            model=ModelType.GPT_4O_MINI
        )
        return agent, "OpenAI GPT-4o-mini"
    
    # 方式3: 指定Anthropic模型
    elif os.getenv('ANTHROPIC_API_KEY'):
        agent = ChatAgent(
            "你是Claude，一个由Anthropic创建的AI助手。",
            model=(ModelPlatformType.ANTHROPIC, ModelType.CLAUDE_3_5_SONNET)
        )
        return agent, "Anthropic Claude-3.5-Sonnet"
    
    # 方式4: 指定Google模型
    elif os.getenv('GOOGLE_API_KEY'):
        agent = ChatAgent(
            "你是Gemini，Google的多模态AI模型。",
            model=("gemini", "gemini-1.5-pro")
        )
        return agent, "Google Gemini-1.5-Pro"
    
    else:
        # 使用默认模型
        agent = ChatAgent("你是一个有用的助手。")
        return agent, "默认模型"

def test_chat_interaction(agent, model_name):
    """测试Chat Agent交互"""
    print(f"\n=== 测试{model_name}交互 ===")
    
    # 测试问题列表
    test_questions = [
        "你好，你是谁？",
        "请介绍一下CAMEL-AI框架。",
        "用Python写一个简单的Hello World程序。",
        "总结一下今天的对话。"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n--- 问题 {i} ---")
        print(f"用户: {question}")
        
        try:
            # 发送消息并获取响应
            response = agent.step(question)
            print(f"助手: {response.msgs[0].content}")
            
        except Exception as e:
            print(f"❌ 错误: {e}")
            continue
    
    print(f"\n✅ {model_name}交互测试完成")

def main():
    """主函数"""
    print("🚀 CAMEL Chat Agent 部署测试")
    print("=" * 50)
    
    # 1. 环境检查
    if not setup_environment():
        return
    
    # 2. 创建并测试Agent
    try:
        agent, model_name = create_specific_model_agent()
        test_chat_interaction(agent, model_name)
        
    except Exception as e:
        print(f"❌ Agent创建失败: {e}")
        print("尝试使用简单Agent...")
        
        try:
            agent = create_simple_agent()
            test_chat_interaction(agent, "简单模型")
        except Exception as e2:
            print(f"❌ 简单Agent也失败: {e2}")
            return
    
    print("\n🎉 Chat Agent部署测试成功完成！")

if __name__ == "__main__":
    main()
