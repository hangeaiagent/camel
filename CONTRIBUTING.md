# 贡献指南

感谢您对Travel AI项目的关注！我们欢迎所有形式的贡献。

## 🚀 如何贡献

### 1. 报告问题
- 搜索现有issues确认问题未被报告
- 使用issue模板提供详细信息
- 包含复现步骤和环境信息

### 2. 功能建议
- 在discussions中讨论新功能想法
- 详细描述功能需求和用例场景
- 等待维护者反馈后再开始开发

### 3. 代码贡献

#### 开发环境设置
```bash
# 克隆仓库
git clone https://github.com/your-username/travel-ai-prototype.git
cd travel-ai-prototype

# 启动开发环境
docker-compose -f docker-compose.dev.yml up -d

# 或者本地开发
cd backend && pip install -r requirements.txt
cd frontend && npm install
```

#### 分支管理
- `main` - 主分支，稳定版本
- `develop` - 开发分支，新功能集成
- `feature/feature-name` - 功能开发分支
- `hotfix/issue-description` - 紧急修复分支

#### 提交规范
使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式：

```
<类型>[可选的作用域]: <描述>

[可选的正文]

[可选的脚注]
```

类型说明：
- `feat`: 新功能
- `fix`: Bug修复
- `docs`: 文档更新
- `style`: 代码格式化
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

#### Pull Request流程
1. Fork项目到个人账户
2. 创建功能分支
3. 完成开发并测试
4. 提交PR到develop分支
5. 等待代码审查
6. 根据反馈修改
7. 合并到主分支

## 📝 代码规范

### Python代码
- 使用Black格式化代码
- 使用isort整理导入
- 通过flake8检查
- 添加类型注解
- 编写文档字符串

```bash
cd backend
black .
isort .
flake8 .
mypy .
```

### TypeScript代码
- 使用ESLint检查
- 使用Prettier格式化
- 严格的TypeScript配置
- 组件props类型定义

```bash
cd frontend
npm run lint
npm run format
npm run type-check
```

### 测试要求
- 新功能必须包含测试
- 保持测试覆盖率 > 80%
- 端到端测试覆盖主要流程

```bash
# 后端测试
cd backend && pytest tests/ -v --cov

# 前端测试  
cd frontend && npm test -- --coverage
```

## 🏗️ 架构指南

### 项目结构
```
travel-ai-prototype/
├── frontend/          # React前端
├── backend/           # FastAPI后端
├── camel_agents/      # CAMEL智能体
├── docker/           # Docker配置
└── docs/             # 文档
```

### 设计原则
- 模块化设计
- 单一职责原则
- 依赖注入
- 错误处理
- 日志记录

### AI智能体开发
- 遵循CAMEL框架规范
- 实现标准接口
- 添加工具包文档
- 编写单元测试

## 🎯 开发优先级

### 高优先级
- [ ] CAMEL框架真实集成
- [ ] 完善测试覆盖
- [ ] 性能优化
- [ ] 安全加固

### 中优先级
- [ ] UI/UX改进
- [ ] 多语言支持
- [ ] API文档完善
- [ ] 监控告警

### 低优先级
- [ ] 移动端适配
- [ ] 主题定制
- [ ] 插件系统
- [ ] 国际化

## 🐛 问题排查

### 常见问题
1. **Docker启动失败**
   - 检查端口占用
   - 确认Docker版本
   - 查看容器日志

2. **依赖安装错误**
   - 更新package.json
   - 清除缓存重装
   - 检查Node/Python版本

3. **数据库连接失败**
   - 确认PostgreSQL运行
   - 检查连接字符串
   - 验证用户权限

### 调试技巧
- 使用IDE断点调试
- 查看容器日志
- 启用详细日志级别
- 使用开发者工具

## 📚 资源链接

- [CAMEL-AI文档](https://docs.camel-ai.org)
- [FastAPI文档](https://fastapi.tiangolo.com)
- [React文档](https://reactjs.org/docs)
- [项目Wiki](https://github.com/your-username/travel-ai-prototype/wiki)

## 🤝 行为准则

请遵守我们的行为准则：
- 尊重他人
- 包容多样性
- 专业讨论
- 及时响应
- 质量优先

## 💬 联系方式

- GitHub Issues: 技术问题和Bug报告
- Discussions: 功能讨论和问答
- Email: dev@travel-ai.com
- Discord: [加入社区](https://discord.gg/travel-ai)

## 🙏 致谢

感谢所有贡献者对项目的支持！

特别感谢：
- [CAMEL-AI团队](https://github.com/camel-ai/camel)提供的多智能体框架
- 开源社区的工具和库支持
- 早期测试用户的宝贵反馈

---

**开始贡献吧！每一个PR都让Travel AI变得更好！** 🚀
