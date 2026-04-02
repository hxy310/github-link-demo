from workflow_engine.cli import command_init, command_plan


def test_cli_init_and_plan(tmp_path, capsys) -> None:
    workflow_path = tmp_path / "workflow.json"

    init_code = command_init(workflow_path)
    assert init_code == 0
    assert workflow_path.exists()

    plan_code = command_plan(workflow_path)
    assert plan_code == 0

    out = capsys.readouterr().out
    assert "lint" in out
    assert "test" in out
    assert "build" in out
