import file_handler

def add_task(task):
    tasks = file_handler.load_tasks()
    tasks.append({"task": task, "done": False})
    file_handler.save_tasks(tasks)

def list_tasks():
    tasks = file_handler.load_tasks()
    return tasks

def remove_task(index):
    tasks = file_handler.load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        file_handler.save_tasks(tasks)

def mark_done(index):
    tasks = file_handler.load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        file_handler.save_tasks(tasks)
