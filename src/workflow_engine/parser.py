from __future__ import annotations

import json
from pathlib import Path

from .models import TaskSpec, WorkflowSpec


class WorkflowParseError(ValueError):
    pass


def load_workflow(path: str | Path) -> WorkflowSpec:
    file_path = Path(path)
    data = json.loads(file_path.read_text(encoding="utf-8"))

    if "tasks" not in data or not isinstance(data["tasks"], list):
        raise WorkflowParseError("workflow file must contain a 'tasks' list")

    tasks: dict[str, TaskSpec] = {}
    for item in data["tasks"]:
        if not isinstance(item, dict):
            raise WorkflowParseError("each task must be an object")
        name = item.get("name")
        command = item.get("command")
        deps = item.get("deps", [])
        if not isinstance(name, str) or not name:
            raise WorkflowParseError("task name must be a non-empty string")
        if not isinstance(command, str) or not command:
            raise WorkflowParseError(f"task {name!r} command must be a non-empty string")
        if not isinstance(deps, list) or any(not isinstance(dep, str) for dep in deps):
            raise WorkflowParseError(f"task {name!r} deps must be a list of strings")
        if name in tasks:
            raise WorkflowParseError(f"duplicate task name: {name}")
        tasks[name] = TaskSpec(name=name, command=command, deps=deps)

    return WorkflowSpec(tasks=tasks)
