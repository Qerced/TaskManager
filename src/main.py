from datetime import datetime
from typing import Annotated, Optional
from typer import Typer, Argument

from models.task import Task, TaskCategory, TaskPriority, TaskStatus

app = Typer()


@app.command()
def get_tasks(category: Annotated[Optional[TaskCategory], Argument()] = None):
    for task in Task.get_all_tasks(category):
        print(task)


@app.command()
def add(
    title: str,
    description: str,
    category: TaskCategory,
    due_date: datetime,
    priority: TaskPriority,
    status: TaskStatus,
):
    Task(title, description, category,
         due_date, priority, status).save()
    print("Задача добавлена!")


@app.command()
def update(
    id: int,
    title: Annotated[Optional[str], Argument()] = None,
    description: Annotated[Optional[str], Argument()] = None,
    category: Annotated[Optional[TaskCategory], Argument()] = None,
    due_date: Annotated[Optional[datetime], Argument()] = None,
    priority: Annotated[Optional[TaskPriority], Argument()] = None,
    status: Annotated[Optional[TaskStatus], Argument()] = None,
):
    Task(title, description, category,
         due_date, priority, status, id).update()
    print("Задача обновлена!")


@app.command()
def delete(
    id: Annotated[Optional[int], Argument()] = None,
    category: Annotated[Optional[TaskCategory], Argument()] = None
):
    Task.delete(id, category)
    print("Задача удалена!")


@app.command()
def find(
    category: Annotated[Optional[TaskCategory], Argument()] = None,
    status: Annotated[Optional[TaskStatus], Argument()] = None
):
    for task in Task.find(category, status):
        print(task)


if __name__ == "__main__":
    app()
