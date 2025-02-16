import task_manager

def run_cli():
    while True:
        cmd = input("Enter command (add/list/remove/done/exit): ").strip().lower()
        if cmd == "add":
            task = input("Enter task: ")
            task_manager.add_task(task)
        elif cmd == "list":
            tasks = task_manager.list_tasks()
            for i, t in enumerate(tasks):
                status = "✔" if t["done"] else "✘"
                print(f"{i}. {status} {t['task']}")
        elif cmd == "remove":
            index = int(input("Enter task index to remove: "))
            task_manager.remove_task(index)
        elif cmd == "done":
            index = int(input("Enter task index to mark done: "))
            task_manager.mark_done(index)
        elif cmd == "exit":
            break
