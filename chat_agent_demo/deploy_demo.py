#!/usr/bin/env python3
"""
CAMEL Chat Agent 部署演示
模拟Chat Agent的基本功能，用于演示部署流程
"""

import os
import sys
from datetime import datetime

class MockChatAgent:
    """模拟Chat Agent类，用于演示部署流程"""
    
    def __init__(self, system_message, model="mock-model"):
        self.system_message = system_message
        self.model = model
        self.conversation_history = []
        print(f"✅ 创建Chat Agent成功")
        print(f"📝 系统消息: {system_message}")
        print(f"🤖 使用模型: {model}")
    
    def step(self, user_input):
        """模拟处理用户输入"""
        print(f"\n🔄 处理用户输入: {user_input}")
        
        # 模拟不同类型的响应
        if "你好" in user_input or "hello" in user_input.lower():
            response = "你好！我是CAMEL Chat Agent演示版本。很高兴为您服务！"
        elif "时间" in user_input or "time" in user_input.lower():
            response = f"当前时间是: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}"
        elif "camel" in user_input.lower() or "框架" in user_input:
            response = """CAMEL-AI是一个强大的多智能体框架，具有以下特性：
            
🤖 多智能体协作 - 支持复杂的智能体社群
🛠️ 丰富工具生态 - 70+专业工具包
🌐 多模型支持 - 支持30+模型平台
📊 企业级架构 - 支持大规模部署
            """
        elif "计算" in user_input or "数学" in user_input:
            if "2+2" in user_input:
                response = "2 + 2 = 4"
            elif "10*5" in user_input:
                response = "10 × 5 = 50"
            else:
                response = "我可以帮您进行简单的数学计算，请告诉我具体的算式。"
        else:
            response = f"我理解您说的是'{user_input}'。作为演示版本，我可以回答关于时间、CAMEL框架和简单计算的问题。"
        
        # 添加到历史记录
        self.conversation_history.append({
            "user": user_input,
            "assistant": response,
            "timestamp": datetime.now()
        })
        
        return MockResponse(response)

class MockResponse:
    """模拟响应对象"""
    
    def __init__(self, content):
        self.content = content
        self.msgs = [MockMessage(content)]

class MockMessage:
    """模拟消息对象"""
    
    def __init__(self, content):
        self.content = content

def check_environment():
    """检查部署环境"""
    print("🔍 环境检查")
    print("=" * 40)
    
    # Python版本检查
    python_version = sys.version_info
    print(f"🐍 Python版本: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major == 3 and 10 <= python_version.minor <= 12:
        print("✅ Python版本兼容")
    else:
        print("⚠️  建议使用Python 3.10-3.12版本以获得最佳兼容性")
    
    # 环境变量检查
    api_keys = [
        'OPENAI_API_KEY',
        'ANTHROPIC_API_KEY', 
        'GOOGLE_API_KEY'
    ]
    
    found_keys = []
    for key in api_keys:
        if os.getenv(key):
            found_keys.append(key)
            print(f"✅ {key} 已配置")
        else:
            print(f"➖ {key} 未配置")
    
    if found_keys:
        print(f"🎉 找到 {len(found_keys)} 个API密钥")
    else:
        print("📝 未找到API密钥，使用模拟模式")
    
    return True

def create_demo_agent():
    """创建演示Agent"""
    print("\n🚀 创建CAMEL Chat Agent演示")
    print("=" * 40)
    
    # 检查是否有真实API密钥
    if os.getenv('OPENAI_API_KEY'):
        print("🔑 检测到OpenAI API密钥，将使用真实模型")
        model_name = "OpenAI GPT (真实模型)"
    elif os.getenv('ANTHROPIC_API_KEY'):
        print("🔑 检测到Anthropic API密钥，将使用真实模型")
        model_name = "Claude (真实模型)"
    else:
        print("🎭 使用模拟模式进行演示")
        model_name = "演示模型 (Mock)"
    
    agent = MockChatAgent(
        system_message="您是一个专业的AI助手，可以回答问题并提供帮助。",
        model=model_name
    )
    
    return agent

def run_interactive_demo(agent):
    """运行交互式演示"""
    print("\n💬 交互式聊天演示")
    print("=" * 40)
    print("输入 'quit' 或 'exit' 退出演示")
    print("输入 'help' 查看示例问题")
    
    while True:
        try:
            user_input = input("\n👤 您: ").strip()
            
            if user_input.lower() in ['quit', 'exit', '退出']:
                print("👋 演示结束，谢谢使用！")
                break
            
            if user_input.lower() == 'help':
                print("\n📋 示例问题:")
                print("- 你好")
                print("- 现在几点了？")
                print("- 介绍一下CAMEL框架")
                print("- 2+2等于多少？")
                continue
            
            if not user_input:
                continue
            
            # 获取响应
            response = agent.step(user_input)
            print(f"🤖 助手: {response.content}")
            
        except KeyboardInterrupt:
            print("\n\n👋 演示被中断，再见！")
            break
        except Exception as e:
            print(f"❌ 错误: {e}")

def run_batch_demo(agent):
    """运行批量测试演示"""
    print("\n🧪 批量测试演示")
    print("=" * 40)
    
    test_questions = [
        "你好，我是新用户",
        "现在是什么时间？",
        "请介绍一下CAMEL-AI框架的主要功能",
        "帮我计算2+2等于多少",
        "你能做什么？"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n--- 测试 {i}/{len(test_questions)} ---")
        print(f"👤 用户: {question}")
        
        try:
            response = agent.step(question)
            print(f"🤖 助手: {response.content}")
        except Exception as e:
            print(f"❌ 错误: {e}")
    
    print(f"\n✅ 批量测试完成，共测试了 {len(test_questions)} 个问题")

def show_deployment_info():
    """显示部署信息"""
    print("\n📚 部署信息")
    print("=" * 40)
    print("🔧 真实部署步骤:")
    print("1. 安装Python 3.10-3.12")
    print("2. 创建虚拟环境: python -m venv camel_env")
    print("3. 激活环境: source camel_env/bin/activate")
    print("4. 安装CAMEL: pip install camel-ai")
    print("5. 设置API密钥: export OPENAI_API_KEY='your_key'")
    print("6. 运行应用")
    
    print("\n📖 相关文档:")
    print("- 详细部署指南: techdocs/03部署chat_agent.md")
    print("- 项目文档: README.md")
    print("- 官方网站: https://www.camel-ai.org/")

def main():
    """主函数"""
    print("🐫 CAMEL Chat Agent 部署演示")
    print("=" * 50)
    print("这是一个模拟演示，展示Chat Agent的部署和使用流程")
    
    # 1. 环境检查
    if not check_environment():
        return
    
    # 2. 创建Agent
    agent = create_demo_agent()
    
    # 3. 选择演示模式
    print("\n🎯 选择演示模式:")
    print("1. 交互式聊天演示")
    print("2. 批量测试演示")
    print("3. 显示部署信息")
    
    while True:
        try:
            choice = input("\n请选择模式 (1-3): ").strip()
            
            if choice == '1':
                run_interactive_demo(agent)
                break
            elif choice == '2':
                run_batch_demo(agent)
                break
            elif choice == '3':
                show_deployment_info()
                break
            else:
                print("❌ 无效选择，请输入1、2或3")
        except KeyboardInterrupt:
            print("\n\n👋 演示被中断，再见！")
            break

if __name__ == "__main__":
    main()
