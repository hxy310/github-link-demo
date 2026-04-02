import json

import pytest

from workflow_engine.parser import WorkflowParseError, load_workflow


def test_load_workflow(tmp_path) -> None:
    file_path = tmp_path / "workflow.json"
    file_path.write_text(
        json.dumps(
            {
                "tasks": [
                    {"name": "lint", "command": "ruff check ."},
                    {"name": "test", "command": "pytest", "deps": ["lint"]},
                ]
            }
        ),
        encoding="utf-8",
    )

    workflow = load_workflow(file_path)

    assert sorted(workflow.tasks.keys()) == ["lint", "test"]
    assert workflow.tasks["test"].deps == ["lint"]


def test_duplicate_task_raises(tmp_path) -> None:
    file_path = tmp_path / "workflow.json"
    file_path.write_text(
        json.dumps(
            {
                "tasks": [
                    {"name": "lint", "command": "ruff check ."},
                    {"name": "lint", "command": "pytest"},
                ]
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(WorkflowParseError):
        load_workflow(file_path)
