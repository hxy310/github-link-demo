from workflow_engine.engine import WorkflowCycleError, WorkflowEngine
from workflow_engine.models import TaskSpec, WorkflowSpec


def test_topological_sort_respects_dependencies() -> None:
    workflow = WorkflowSpec(
        tasks={
            "lint": TaskSpec(name="lint", command="ruff check ."),
            "test": TaskSpec(name="test", command="pytest", deps=["lint"]),
            "build": TaskSpec(name="build", command="python -m build", deps=["test"]),
        }
    )

    engine = WorkflowEngine(workflow)
    order = [task.name for task in engine.topological_sort()]

    assert order == ["lint", "test", "build"]


def test_cycle_detection() -> None:
    workflow = WorkflowSpec(
        tasks={
            "a": TaskSpec(name="a", command="echo a", deps=["b"]),
            "b": TaskSpec(name="b", command="echo b", deps=["a"]),
        }
    )

    engine = WorkflowEngine(workflow)

    try:
        engine.topological_sort()
    except WorkflowCycleError:
        assert True
    else:
        raise AssertionError("expected cycle detection")
