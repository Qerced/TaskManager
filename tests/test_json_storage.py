import json

from src.storage.json_storage import JsonStorage


def test_json_storage_initialization(tmp_json):
    JsonStorage(tmp_json)
    assert tmp_json.exists()
    with open(tmp_json, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert data == []


def test_json_storage_read_write(task_storage, tmp_json):
    tmp_storage = JsonStorage(tmp_json)
    tmp_storage.write(task_storage)
    assert tmp_storage.read() == task_storage
