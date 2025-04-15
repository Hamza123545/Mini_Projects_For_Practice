# simple todo list mini project

print("welcome to the todo list mini project!")


todo_list = []

def show_menu():
    print("1. Add Task")
    print("2. view task")
    print("3. Exit")


def todo_app():
    while True:
        show_menu()
        choice = input("Enter your choice (1/3)")

        if choice == "1":
            task = input("Enter your task: ")
            todo_list.append(task)
            print("task added")

        elif choice == "2":
            print("your task?")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
        elif choice == "3":
            print("Good Bye")

            break

        else:
            print("Invalid choice")


todo_app()
