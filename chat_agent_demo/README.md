# CAMEL Chat Agent 演示

这是一个基于CAMEL-AI框架的Chat Agent部署演示项目。

## 快速开始

### 1. 环境准备
```bash
# 确保Python版本在3.10-3.12之间
python --version

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置API密钥
```bash
# 复制环境配置模板
cp env_example.txt .env

# 编辑.env文件，添加你的API密钥
nano .env
```

### 4. 运行示例
```bash
# 运行简单Chat Agent
python simple_chat_agent.py
```

## 支持的模型平台

- ✅ OpenAI (GPT-4, GPT-4o, GPT-3.5)
- ✅ Anthropic (Claude-3.5-Sonnet)
- ✅ Google (Gemini-1.5-Pro)
- ✅ Azure OpenAI
- ✅ 智谱AI (GLM系列)
- ✅ 阿里千问 (Qwen系列)
- ✅ 深度求索 (DeepSeek)
- ✅ 月之暗面 (Moonshot)

## 文件说明

- `simple_chat_agent.py`: 基础Chat Agent示例
- `requirements.txt`: Python依赖包
- `env_example.txt`: 环境变量配置模板
- `README.md`: 项目说明文档

## 常见问题

### Q: 如何获取API密钥？
A: 
- OpenAI: https://platform.openai.com/account/api-keys
- Anthropic: https://console.anthropic.com/
- Google: https://makersuite.google.com/app/apikey

### Q: 遇到模型访问错误怎么办？
A: 
1. 检查API密钥是否正确
2. 确认账户有足够余额
3. 验证网络连接正常

### Q: 如何切换不同的模型？
A: 修改代码中的模型配置或设置相应的环境变量。

## 技术支持

详细的部署指南请参考：`techdocs/03部署chat_agent.md`

## 许可证

Apache 2.0 License
