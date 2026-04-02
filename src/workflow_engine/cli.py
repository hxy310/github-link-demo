from __future__ import annotations

import argparse
import json
from pathlib import Path

from .engine import WorkflowEngine
from .parser import load_workflow

EXAMPLE = {
    "tasks": [
        {"name": "lint", "command": "ruff check ."},
        {"name": "test", "command": "pytest", "deps": ["lint"]},
        {"name": "build", "command": "python -m build", "deps": ["test"]},
    ]
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Workflow engine demo CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    explain_parser = subparsers.add_parser("plan", help="Print workflow execution order")
    explain_parser.add_argument("workflow", type=Path, help="Path to workflow JSON file")

    init_parser = subparsers.add_parser("init", help="Write an example workflow file")
    init_parser.add_argument("output", type=Path, help="Where to write the example JSON")

    return parser


def command_plan(workflow_path: Path) -> int:
    workflow = load_workflow(workflow_path)
    engine = WorkflowEngine(workflow)
    for index, task in enumerate(engine.topological_sort(), start=1):
        print(f"{index}. {task.name}: {task.command}")
    return 0


def command_init(output_path: Path) -> int:
    output_path.write_text(json.dumps(EXAMPLE, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Example workflow written to {output_path}")
    return 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "plan":
        return command_plan(args.workflow)
    if args.command == "init":
        return command_init(args.output)
    parser.error("unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
