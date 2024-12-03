from datetime import datetime
from enum import Enum
from typing import Any, Optional

from storage.json_storage import JsonStorage


class TaskPriority(Enum):
    LOW = "Низкий"
    MIDDLE = "Средний"
    HIGH = "Высокий"


class TaskCategory(Enum):
    WORK = "Работа"
    PERSONAL = "Личное"
    STUDY = "Обучение"


class TaskStatus(Enum):
    NOT_COMPLETED = "Не выполнена"
    IN_PROGRESS = "В работе"
    COMPLETED = "Выполнена"


class Task:
    _storage: JsonStorage = JsonStorage("data/tasks.json")

    def __init__(
        self,
        title: str,
        description: str,
        category: TaskCategory,
        due_date: datetime,
        priority: TaskPriority,
        status: TaskStatus,
        id: Optional[int] = None,
    ):
        self.id = id if id else Task.generate_id()
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category.value,
            "due_date": self.due_date.isoformat(),
            "priority": self.priority.value,
            "status": self.status.value,
        }

    def save(self):
        tasks = self._storage.read()
        tasks.append(self.to_dict())
        self._storage.write(tasks)

    def update(self):
        tasks = self._storage.read()
        for index, task in enumerate(tasks):
            if task["id"] == self.id:
                for key, value in self.to_dict().items():
                    if value:
                        tasks[index][key] = value
                self._storage.write(tasks)
                return
        raise ValueError(f"Задача с id {self.id} не найдена.")

    @classmethod
    def generate_id(cls) -> int:
        tasks = cls._storage.read()
        if tasks:
            return max(task["id"] for task in tasks) + 1
        return 1

    @classmethod
    def find(
        cls,
        category: Optional[TaskCategory] = None,
        status: Optional[TaskStatus] = None
    ) -> list[dict]:
        return [
            task
            for task in cls._storage.read()
            if (not category or task["category"] == category.value)
            and (not status or task["status"] == status.value)
        ]

    @classmethod
    def delete(
        cls,
        id: Optional[int] = None,
        category: Optional[TaskCategory] = None
    ):
        tasks = cls._storage.read()
        if id:
            tasks = [task for task in tasks if task["id"] != id]
        elif category:
            tasks = [task for task in tasks
                     if task["category"] != category.value]
        else:
            raise ValueError(
                "Необходимо передать id или категорию для удаления."
            )
        cls._storage.write(tasks)

    @classmethod
    def get_all_tasks(
        cls, category: Optional[TaskCategory] = None
    ) -> list[dict]:
        tasks = cls._storage.read()
        if category:
            return [task for task in tasks
                    if task["category"] == category.value]
        return tasks
