# Task Tracker CLI

A simple **Command Line Interface (CLI)** application to create, edit, and manage tasks using Python.
Tasks are stored locally in a JSON file.

---

# Requirements

* Python **3.8+**
* No external libraries required (only Python standard library)

---

# Installation

1. Clone or download the project.

2. Navigate to the project folder:

```
cd task-tracker
```

3. Run the program using Python:

```
python main.py
```

---

# Commands

The program supports the following commands:

* **add** -> create a new task
* **edit** -> modify an existing task
* **rm** -> remove a task
* **list** -> list all tasks
* **listDone** -> list all done tasks
* **listUndone** -> list all undone tasks 

---

# Add a Task

Create a new task by providing a task name and description.

```
python main.py add "Task name" "Task description"
```

### Example

```
python main.py add "Study Python" "Practice argparse and JSON"
```

Output example:

```
Task successfully created! It's ID: 1
```

---

# Edit a Task

Modify a task using its ID.

You can change:

* the name
* the description
* the status

```
python main.py edit <id> [--name "..."] [--description "..."] [--status "..."]
```

### Examples

Change the task name:

```
python main.py edit 1 --name "Study Algorithms"
```

Change the description:

```
python main.py edit 1 --description "Practice dynamic programming"
```

Change the status:

```
python main.py edit 1 --status "done"
```

Edit multiple fields:

```
python main.py edit 1 --name "Study Graphs" --status "in-progress"
```

---

# Remove a Task

Delete a task using its ID.

```
python main.py rm <id>
```

### Example

```
python main.py rm 1
```

Output:

```
Task has been removed.
```

---

# Task Storage

Tasks are stored in a file called:

```
task.json
```

Example structure:

```json
{
    "last_id": 2,
    "tasks": {
        "1": {
            "created_at": "Mon Mar 10",
            "task_name": "Study Python",
            "description": "Practice argparse",
            "status": "todo"
        }
    }
}
```

---

# Status Suggestions

Common status values:

* `todo`
* `in-progress`
* `done`

---

# Project Structure

```
task-tracker/
│
├── main.py
├── functions.py
├── task.json
└── README.md
```

---

# Future Improvements

Possible improvements for the project:


* colored ter
