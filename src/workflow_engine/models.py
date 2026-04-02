from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class TaskSpec:
    name: str
    command: str
    deps: list[str] = field(default_factory=list)


@dataclass(slots=True)
class WorkflowSpec:
    tasks: dict[str, TaskSpec]
