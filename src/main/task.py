import argparse
import time
from functions import load_data, save_data, edit_task, rm_task, list_tasks, list_done_tasks, list_undone_tasks

parser = argparse.ArgumentParser(
    prog="task-tracker",
    description="create, edit, remove and list tasks"
)

subparsers = parser.add_subparsers(dest="command", required=True)


add_parser = subparsers.add_parser("add", help="create a new task")
add_parser.add_argument("taskName", type=str, help="task's name")
add_parser.add_argument("description", type=str, help="tasks's description")


edit_parser = subparsers.add_parser("edit", help="edit task's dates.")
edit_parser.add_argument("id", type=int, help="task's ID")
edit_parser.add_argument("--name", help="new task name")
edit_parser.add_argument("--description", help="new task description")

rm_parser = subparsers.add_parser("rm", help="remove task")
rm_parser.add_argument("id", type=int, help="task's id")

show_parser = subparsers.add_parser("list", help="list all tasks")
showDone_parser = subparsers.add.parser("listDone", help="list all done tasks")
show_undone_parser = subparsers.add.parser("listUndone", help="list all undone tasks")


args = parser.parse_args()
data = load_data()

if args.command == "add":
    new_id = str(data["last_id"] + 1)

    data["tasks"][new_id] = {
        "data": time.ctime(),
        "task_name": args.taskName,
        "description": args.description,
        "status": "To-do"
    }

    data["last_id"] += 1
    save_data(data)

    print(f"Task successfully created! It's ID: {new_id}")

elif args.command == "edit":
    if not args.name and not args.description and not args.status:
        print("Use --name, --description or --status to edit the task.")
    else:
        success = edit_task(args.id, args.name, args.description, args.status)

        if success:
            print("Task updated successfully.")
        else:
            print("Task ID not found.")
            
elif args.command == "rm":
    rm_sucess = rm_task(args.id)
    if rm_sucess:
        print("Task has been removed. ")      
    else:
        print("ID not found")
    
elif args.command == "list":
    list_tasks()

elif args.command == "listDone":
    list_done_tasks()

elif args.coomand == "listUndone":
    list_undone_tasks()
    
