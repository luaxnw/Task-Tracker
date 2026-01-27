import argparse
import time
from function import load_data, save_data, edit_task

parser = argparse.ArgumentParser(
    prog="Task-Tracker",
    description="Create and edit tasks"
)

subparsers = parser.add_subparsers(dest="command", required=True)


add_parser = subparsers.add_parser("add", help="Criar nova task")
add_parser.add_argument("taskName", type=str, help="Nome da task")
add_parser.add_argument("description", type=str, help="Descrição da task")


edit_parser = subparsers.add_parser("edit", help="Editar task existente")
edit_parser.add_argument("id", type=int, help="ID da task")
edit_parser.add_argument("--name", help="Novo nome da task")
edit_parser.add_argument("--description", help="Nova descrição da task")


args = parser.parse_args()
data = load_data()

if args.command == "add":
    new_id = str(data["last_id"] + 1)

    data["tasks"][new_id] = {
        "Data": time.ctime(),
        "Task Name": args.taskName,
        "Description": args.description
    }

    data["last_id"] += 1
    save_data(data)

    print(f"Task successfully created! It's ID: {new_id}")

elif args.command == "edit":
    if not args.name and not args.description:
        print("Try --name or description. ")
    else:
        success = edit_task(args.id, args.name, args.description)

        if success:
            print("Task has been changed. ")
        else:
            print("ID not found")
