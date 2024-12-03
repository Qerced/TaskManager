from pathlib import Path

import pytest

from src.storage.json_storage import JsonStorage


@pytest.fixture
def task_add_cli():
    return [
        "add",
        "Изучить основы FastAPI",
        "Пройти документацию по FastAPI и создать простой проект",
        "Обучение",
        "2024-11-30",
        "Высокий",
        "Не выполнена"
    ]


@pytest.fixture
def task_update_cli():
    return [
        "update",
        "1",
        "Изучить основы FastAPI",
        "Пройти документацию по FastAPI и создать простой проект",
        "Работа",
        "2024-11-30",
        "Высокий",
        "Выполнена"
    ]


@pytest.fixture
def task_delete_cli():
    return [
        "delete",
        "1"
    ]


@pytest.fixture
def task_find_cli():
    return [
        "find",
        "Работа",
        "Выполнена"
    ]


@pytest.fixture
def task_get_cli():
    return [
        "get-tasks",
        "Обучение"
    ]


@pytest.fixture
def task_storage():
    return {
        "id": 1,
        "title": "Изучить основы FastAPI",
        "description": "Пройти документацию по FastAPI и создать простой проект",
        "category": "Обучение",
        "due_date": "2024-11-30T00:00:00",
        "priority": "Высокий",
        "status": "Не выполнена"
    }


@pytest.fixture
def task_storage_updated():
    return {
        "id": 1,
        "title": "Изучить основы FastAPI",
        "description": "Пройти документацию по FastAPI и создать простой проект",
        "category": "Работа",
        "due_date": "2024-11-30T00:00:00",
        "priority": "Высокий",
        "status": "Выполнена"
    }


@pytest.fixture
def tmp_json():
    temp_file = Path("data/test_tasks.json")
    yield temp_file
    if temp_file.exists():
        temp_file.unlink()
