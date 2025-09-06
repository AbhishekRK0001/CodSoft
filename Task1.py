# its a very simple task manager , tooo simple and easy because i was still learning this language

tasks = []

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})

def show_tasks():
    if not tasks:
        print("No tasks yet")
    else:
        for i in range(len(tasks)):
            status = "done" if tasks[i]["done"] else "not done"
            print(i+1, ".", tasks[i]["title"], "-", status)

def mark_done():
    show_tasks()
    num = int(input("Enter task number to mark done: ")) - 1
    if 0 <= num < len(tasks):
        tasks[num]["done"] = True
    else:
        print("Invalid number")

def delete_task():
    show_tasks()
    num = int(input("Enter task number to delete: ")) - 1
    if 0 <= num < len(tasks):
        tasks.pop(num)
    else:
        print("Invalid number")

while True:
    print("\n1. Add a Task")
    print("2. Show the Tasks")
    print("3. Mark the Task as Done")
    print("4. Delete a Task")
    print("5. Exit Menu")

    choice = input("Choose: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Finish tata Bye Bye ")
        break
    else:
        print("Wrong choice")
