# 工作流引擎测试项目

这是一个比普通 Hello World 更复杂的测试项目，用于演示如何把一个 **真实一点的 Python 项目** 与 **GitHub Actions** 结合起来。

## 项目目标

本项目实现了一个轻量级的 **DAG 工作流执行计划引擎**，支持：
- 从 JSON 读取任务定义
- 校验任务结构
- 根据依赖关系进行拓扑排序
- 通过 CLI 输出任务执行顺序

它适合拿来测试：
- 单元测试
- 代码风格检查
- 类型检查
- 打包构建
- 多工作流 GitHub Actions

## 项目结构

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── pull_request_template.md
│   └── workflows/
│       ├── ci.yml
│       └── release-check.yml
├── src/
│   └── workflow_engine/
│       ├── __init__.py
│       ├── cli.py
│       ├── engine.py
│       ├── models.py
│       └── parser.py
├── tests/
│   ├── test_engine.py
│   └── test_parser.py
├── workflow.example.json
├── pyproject.toml
├── main.py
└── README.md
```

## 本地运行

### 1. 安装开发依赖
```bash
python3 -m pip install -e .[dev]
```

### 2. 生成示例工作流
```bash
python3 main.py init workflow.json
```

### 3. 输出执行计划
```bash
python3 main.py plan workflow.json
```

输出示例：
```text
1. lint: ruff check .
2. test: pytest
3. build: python -m build
```

## 本地质量检查

### Ruff
```bash
ruff check .
```

### Mypy
```bash
mypy src
```

### Pytest
```bash
pytest
```

### Build
```bash
python -m build
```

## GitHub Actions

当前仓库将使用 GitHub Actions 完成：
- Push / PR 自动运行 lint + type check + test
- 构建源码包和 wheel
- 上传构建产物
- 单独提供 release-check 工作流

## 后续可扩展方向

- 支持 YAML 配置
- 支持真正执行命令
- 支持并行任务调度
- 支持失败重试策略
- 支持任务图可视化
