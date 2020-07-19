from fastapi import BackgroundTasks
from config import app
import time
from datetime import datetime
import constant


def _run_task(name: str, id=None):
    time.sleep(3)
    with open('tasks_out.txt', mode='a') as file:
        now = datetime.now()
        content = f'{name}  [{id}]:  {now}'
        file.write(content)


@app.post('/tasks/run/{name}/{id}')
async def task_run(name: str, id: int, background_task: BackgroundTasks):
    """ takes a task and writes into a file"""
    background_task.add_task(_run_task, name, id)
    return {constant.MESSAGE: f'Task {name} with ID {id} is being run...'}
