# GitHub部署指南

## 🚀 推送到GitHub的步骤

### 1. 创建新的GitHub仓库

**在GitHub网站上操作：**

1. 登录到您的GitHub账户
2. 点击右上角的 "+" 按钮，选择 "New repository"
3. 填写仓库信息：
   - **Repository name**: `travel-ai-prototype`
   - **Description**: `🧳 Intelligent Travel Planning Engine - A multi-agent AI system built with CAMEL-AI framework for conversational travel planning`
   - **Visibility**: Public (建议) 或 Private
   - **不要勾选** "Add a README file" (我们已经有了)
   - **不要勾选** "Add .gitignore" (我们已经有了)
   - **不要勾选** "Choose a license" (我们已经有了)

4. 点击 "Create repository"

### 2. 连接本地仓库到GitHub

**在终端中执行以下命令：**

```bash
# 确保在项目根目录
cd /Users/a1/work/camel/travel-ai-prototype

# 添加远程仓库 (替换YOUR_USERNAME为您的GitHub用户名)
git remote add origin https://github.com/YOUR_USERNAME/travel-ai-prototype.git

# 推送到GitHub
git push -u origin main
```

### 3. 验证推送成功

推送完成后，您的GitHub仓库应该包含：

- ✅ 完整的项目代码 (49个文件)
- ✅ README.md 文档
- ✅ CI/CD 配置 (.github/workflows/)
- ✅ 许可证 (LICENSE)
- ✅ 贡献指南 (CONTRIBUTING.md)
- ✅ Docker 配置文件

## 🔧 配置GitHub仓库

### 设置仓库密钥 (Secrets)

为了让CI/CD正常工作，需要在GitHub仓库设置中添加以下密钥：

1. 进入仓库页面
2. 点击 "Settings" 标签
3. 左侧菜单选择 "Secrets and variables" > "Actions"
4. 点击 "New repository secret" 添加：

```
OPENAI_API_KEY=your-openai-api-key-here
ANTHROPIC_API_KEY=your-anthropic-api-key-here
```

### 启用GitHub Pages (可选)

如果要部署项目文档：

1. 在Settings中找到 "Pages"
2. Source选择 "Deploy from a branch"
3. Branch选择 "main"，文件夹选择 "docs"
4. 点击Save

### 配置分支保护规则

为了确保代码质量：

1. 进入 "Settings" > "Branches"
2. 点击 "Add rule"
3. Branch name pattern: `main`
4. 勾选以下选项：
   - "Require a pull request before merging"
   - "Require status checks to pass before merging"
   - "Require branches to be up to date before merging"
   - "Include administrators"

## 📊 监控和管理

### GitHub Actions

推送后，以下工作流会自动运行：

1. **Backend Tests** - Python后端测试
2. **Frontend Tests** - React前端测试
3. **Code Quality** - 代码格式和质量检查
4. **Security Scan** - 安全漏洞扫描

在 "Actions" 标签页查看运行状态。

### Issues和Project管理

建议设置：

1. **Labels**: 为issue创建标签体系
   - `bug` - Bug报告
   - `feature` - 新功能
   - `documentation` - 文档相关
   - `good first issue` - 适合新贡献者

2. **Templates**: 创建issue和PR模板
3. **Projects**: 使用GitHub Projects跟踪开发进度

## 🌟 推广仓库

### 仓库描述优化

在仓库主页设置：

- **Description**: `🧳 Intelligent Travel Planning Engine - Multi-agent AI system with CAMEL-AI framework`
- **Website**: `https://your-username.github.io/travel-ai-prototype`
- **Topics**: `ai`, `travel`, `camel-ai`, `multi-agent`, `fastapi`, `react`, `typescript`, `python`

### README徽章

在README.md顶部添加状态徽章：

```markdown
![CI](https://github.com/YOUR_USERNAME/travel-ai-prototype/workflows/CI/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Node](https://img.shields.io/badge/node-18+-green.svg)
```

## 🚀 部署选项

### 1. Docker Hub (推荐)

```bash
# 构建并推送Docker镜像
docker build -t your-username/travel-ai-backend ./backend
docker build -t your-username/travel-ai-frontend ./frontend

docker push your-username/travel-ai-backend
docker push your-username/travel-ai-frontend
```

### 2. Heroku部署

```bash
# 安装Heroku CLI后
heroku create travel-ai-prototype
git push heroku main
```

### 3. Vercel部署 (前端)

1. 连接GitHub仓库到Vercel
2. 设置构建命令：`cd frontend && npm run build`
3. 设置输出目录：`frontend/dist`

### 4. Railway/Render部署 (全栈)

连接GitHub仓库自动部署。

## 📝 后续维护

### 定期更新

1. **依赖更新**: 定期更新package.json和requirements.txt
2. **安全补丁**: 关注GitHub安全警告
3. **CAMEL框架**: 跟进CAMEL-AI的更新

### 社区建设

1. **文档维护**: 保持README和文档的更新
2. **Issue回复**: 及时回复用户问题
3. **PR审查**: 认真审查社区贡献
4. **版本发布**: 定期发布稳定版本

## 🎯 成功指标

仓库设置成功的标志：

- ✅ CI/CD全部通过 
- ✅ 代码覆盖率 > 80%
- ✅ 文档完整清晰
- ✅ 安全扫描通过
- ✅ Docker镜像构建成功

---

**准备好推送到GitHub了！** 🚀

现在执行：
```bash
git remote add origin https://github.com/YOUR_USERNAME/travel-ai-prototype.git
git push -u origin main
```
