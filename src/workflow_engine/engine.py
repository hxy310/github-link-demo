from __future__ import annotations

from collections import deque

from .models import TaskSpec, WorkflowSpec


class WorkflowCycleError(ValueError):
    pass


class WorkflowEngine:
    def __init__(self, workflow: WorkflowSpec) -> None:
        self.workflow = workflow

    def topological_sort(self) -> list[TaskSpec]:
        tasks = self.workflow.tasks
        indegree: dict[str, int] = {name: 0 for name in tasks}
        graph: dict[str, list[str]] = {name: [] for name in tasks}

        for task in tasks.values():
            for dep in task.deps:
                if dep not in tasks:
                    raise KeyError(f"task {task.name!r} depends on missing task {dep!r}")
                graph[dep].append(task.name)
                indegree[task.name] += 1

        queue = deque(sorted(name for name, degree in indegree.items() if degree == 0))
        order: list[TaskSpec] = []

        while queue:
            name = queue.popleft()
            order.append(tasks[name])
            for next_task in sorted(graph[name]):
                indegree[next_task] -= 1
                if indegree[next_task] == 0:
                    queue.append(next_task)

        if len(order) != len(tasks):
            raise WorkflowCycleError("cycle detected in workflow")

        return order
