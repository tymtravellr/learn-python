### ------ TODO APP IN PYTHON ------ ###

# Step 1: Create a new todo
myTodo = ["Coding"]

def add_todo():
    task = str(input("Enter your todo name: "))
    myTodo.append(task)
    print("New Todo Added", myTodo)

def del_todo():
    task = str(input("Enter your todo name: "))
    myTodo.remove(task)
    print("Todo deleted successfully", myTodo)

def update_todo():
    for todo in myTodo:
        print(todo)
    task = str(input("Which one do you want to update: "))
    newTodo = str(input("update todo: "))
    myTodo[myTodo.index(task)] = newTodo
    print("Todo updated successfully: ", myTodo)

def view_todo():
    print("All Todos:")
    for todo in myTodo:
        print(f"{myTodo.index(todo) + 1}: {todo}")

def main():
    while True:
        print("1. Add Todo")
        print("2. Delete Todo")
        print("3. Update Todo")
        print("4. View Todo")
        command = int(input("Enter command: "))
        if command == 1:
            add_todo()
        elif command == 2:
            del_todo()
        elif command == 3:
            update_todo()
        elif command == 4:
            view_todo()
        else:
            print("Something went wrong")

main()