from typer.testing import CliRunner

from src.main import app

runner = CliRunner()


def test_add(task_add_cli):
    result = runner.invoke(app, task_add_cli)
    assert result.exit_code == 0
    assert "Задача добавлена!" in result.stdout


def test_get_tasks(task_get_cli, task_storage):
    result = runner.invoke(app, task_get_cli)
    assert result.exit_code == 0
    assert str(task_storage)+"\n" == result.stdout


def test_update_tasks(task_update_cli):
    result = runner.invoke(app, task_update_cli)
    assert result.exit_code == 0
    assert "Задача обновлена!\n" == result.stdout


def test_find_tasks(task_find_cli, task_storage_updated):
    result = runner.invoke(app, task_find_cli)
    assert result.exit_code == 0
    assert str(task_storage_updated) + "\n" == result.stdout


def test_delete_tasks(task_delete_cli):
    result = runner.invoke(app, task_delete_cli)
    assert result.exit_code == 0
    assert "Задача удалена!\n" == result.stdout
