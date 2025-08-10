# Travel AI Prototype - CAMEL Framework Integration Notes

## 🎯 项目说明

这是一个基于 [CAMEL-AI框架](https://github.com/camel-ai/camel) 构建的智能旅游规划应用原型，展示了如何使用CAMEL的多智能体架构来构建实际的商业应用。

## 🏗️ 与CAMEL框架的关系

### 使用的CAMEL组件
- **Workforce**: 多智能体协作系统
- **RolePlayingWorker**: 专业化智能体角色
- **Toolkits**: 自然语言处理、搜索、翻译等工具包
- **ModelFactory**: 多AI模型支持

### 项目特色
- **5个专业智能体**: 对话、规划、路线、数据、质量评估
- **现代化技术栈**: React + FastAPI + PostgreSQL + Docker
- **实时通信**: WebSocket支持的流式对话
- **完整的工程实践**: CI/CD、测试、文档

## 🚀 运行项目

```bash
# 克隆项目
git clone https://github.com/hangeaiagent/camel.git
cd camel
git checkout travel-ai-prototype

# 启动开发环境
docker-compose -f docker-compose.dev.yml up -d

# 访问应用
# 前端: http://localhost:3000
# 后端: http://localhost:8000
```

## 📚 相关文档

- **技术方案**: `techdocs/06对话式AI规划引擎技术方案.md`
- **开发计划**: `techdocs/07对话AI引擎原型开发计划.md`
- **任务总结**: `techdocs/08开发任务完成总结1-1.md`
- **部署指南**: `DEPLOYMENT_GUIDE.md`

## 🤝 贡献指南

本项目作为CAMEL框架的应用示例，欢迎：
- 功能改进和扩展
- CAMEL框架集成优化
- 文档和教程完善
- Bug修复和性能优化

## 📞 联系方式

- 技术问题: GitHub Issues
- 功能建议: GitHub Discussions
- 邮箱: dev@travel-ai.com

---

**这是一个展示CAMEL-AI框架强大能力的实际应用项目！** 🐫
