# GitHub 链接示例项目

这是一个用于演示 **本地项目如何连接并推送到 GitHub** 的最小示例仓库。

## 项目说明

本项目包含一个简单的 Python 程序：

```python
print("Hello, GitHub!")
```

适合用于：
- 测试 Git 与 GitHub 的连接是否正常
- 验证 SSH 推送是否成功
- 演示最基础的仓库初始化流程
- 作为后续扩展项目的起点

## 目录结构

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── LICENSE
├── README.md
└── main.py
```

## 本地运行

请确保已安装 Python 3，然后执行：

```bash
python3 main.py
```

如果运行成功，你会看到：

```text
Hello, GitHub!
```

## GitHub Actions

本仓库已配置一个基础的 GitHub Actions 工作流，在以下场景自动执行：
- push 到 `main` 分支
- 提交 Pull Request 到 `main` 分支

工作流会完成以下内容：
1. 拉取代码
2. 安装 Python
3. 运行 `main.py`

## 后续可扩展方向

你可以在这个仓库基础上继续扩展，例如：
- 增加 Python 包结构
- 添加单元测试
- 接入代码格式化检查
- 配置自动发布流程
- 增加 Issue / PR 模板

## 许可证

本项目采用 MIT License。
