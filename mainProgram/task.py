import argparse
import time
from functions import load_data, save_data, edit_task, rm_task, list_tasks

parser = argparse.ArgumentParser(
    prog="task-tracker",
    description="create, edit, remove and list tasks"
)

subparsers = parser.add_subparsers(dest="command", required=True)


add_parser = subparsers.add_parser("add", help="create a new task")
add_parser.add_argument("taskName", type=str, help="task's name")
add_parser.add_argument("description", type=str, help="tasks's description")


<<<<<<< HEAD



edit_parser = subparsers.add_parser("edit", help="Editar task existente")
edit_parser.add_argument("id", type=int, help="ID da task")
edit_parser.add_argument("--name", help="Novo nome da task")
edit_parser.add_argument("--description", help="Nova descrição da task")
edit_parser.add_argument("--status", help="Novo status da task")
=======
edit_parser = subparsers.add_parser("edit", help="edit task's dates.")
edit_parser.add_argument("id", type=int, help="task's ID")
edit_parser.add_argument("--name", help="new task name")
edit_parser.add_argument("--description", help="new task description")
>>>>>>> dadace4cfbf3b1401486fb2ad97b0c1230afe5fd

rm_parser = subparsers.add_parser("rm", help="remove task")
rm_parser.add_argument("id", type=int, help="task's id")

show_parser = subparsers.add_parser("list",help="list all tasks")
<<<<<<< HEAD


=======
show_parser.add_argument("show")
>>>>>>> dadace4cfbf3b1401486fb2ad97b0c1230afe5fd


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
