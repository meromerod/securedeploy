from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="SecureDeploy API")


class Task(BaseModel):
    title: str
    completed: bool = False


tasks = []


@app.get("/")
def root():
    return {
        "message": "SecureDeploy API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(new_task)

    return new_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {
                "message": "Task deleted"
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )