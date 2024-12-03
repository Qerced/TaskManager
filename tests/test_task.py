from datetime import datetime
from src.models.task import Task, TaskCategory, TaskPriority, TaskStatus
from src.storage.json_storage import JsonStorage


def test_task_creation():
    task = Task(
        title="Test Task",
        description="This is a test",
        category=TaskCategory.WORK,
        due_date=datetime(2024, 12, 1),
        priority=TaskPriority.HIGH,
        status=TaskStatus.NOT_COMPLETED,
    )
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.category == TaskCategory.WORK
    assert task.priority == TaskPriority.HIGH
    assert task.status == TaskStatus.NOT_COMPLETED


def test_task_save_and_read(tmp_json):
    task = Task
    task._storage = JsonStorage(tmp_json)
    task(
        title="Save Task",
        description="Save test",
        category=TaskCategory.STUDY,
        due_date=datetime(2024, 12, 1),
        priority=TaskPriority.LOW,
        status=TaskStatus.IN_PROGRESS,
    ).save()
    tasks = task.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Save Task"


def test_task_update(tmp_json):
    task = Task
    task._storage = JsonStorage(tmp_json)
    task(
        id=1,
        title="Update Task",
        description="Initial description",
        category=TaskCategory.PERSONAL,
        due_date=datetime(2024, 12, 1),
        priority=TaskPriority.MIDDLE,
        status=TaskStatus.NOT_COMPLETED,
    ).save()
    task(
        id=1,
        title="Updated Task",
        description="Updated description",
        category=TaskCategory.PERSONAL,
        due_date=datetime(2024, 12, 2),
        priority=TaskPriority.HIGH,
        status=TaskStatus.IN_PROGRESS,
    ).update()
    tasks = Task.get_all_tasks()
    assert tasks[0]["title"] == "Updated Task"
    assert tasks[0]["description"] == "Updated description"
    assert tasks[0]["priority"] == TaskPriority.HIGH.value


def test_task_delete(tmp_json):
    task = Task
    task._storage = JsonStorage(tmp_json)
    task(
        id=1,
        title="Delete Task",
        description="Delete test",
        category=TaskCategory.WORK,
        due_date=datetime(2024, 12, 1),
        priority=TaskPriority.LOW,
        status=TaskStatus.NOT_COMPLETED,
    ).save()
    task.delete(id=1)
    tasks = Task.get_all_tasks()
    assert len(tasks) == 0
