import json
import os
# Define the file where the to-do list will be stored
FILE_NAME = "todo_list.json"
# Function to load the to-do list from a file
def load_todo_list():
if os.path.exists(FILE_NAME):
with open(FILE_NAME, "r") as file:
  return json.load(file)
      return []
      # Function to save the to-do list to a file
    def save_todo_list(todo_list):
      with open(FILE_NAME, "w") as file:
        json.dump(todo_list, file, indent=4)
# Function to display the to-do list
def display_todo_list(todo_list):
  if not todo_list:
    print("Your to-do list is empty.")
  else:
    print("Your to-do list:")
    for index, task in enumerate(todo_list, start=1):
      status = "Done" if task["completed"] else "Pending"
      print(f"{index}. {task['task']} [{status}]")

# Function to add a new task to the to-do list
def add_task(todo_list):
  task = input("Enter the new task: ")
  todo_list.append({"task": task, "completed": False})
  save_todo_list(todo_list)
  print("Task added successfully!")

# Function to mark a task as completed
def mark_task_completed(todo_list):
  task_number = int(input("Enter the task number to mark as completed: "))
  if 1 <= task_number <= len(todo_list):
  todo_list[task_number - 1]["completed"] = True
  save_todo_list(todo_list)print("Task marked as completed!")
    else:
      print("Invalid task number.")

# Function to delete a task from the to-do list
def delete_task(todo_list):
task_number = int(input("Enter the task number to delete: "))
if 1 <= task_number <= len(todo_list):
del todo_list[task_number - 1]
save_todo_list(todo_list)
print("Task deleted successfully!")
    else:
print("Invalid task number.")

# Main function to run the To-Do List application
def main():
    todo_list = load_todo_list()
  while True:
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
      display_todo_list(todo_list)
    elif choice == "2":
      add_task(todo_list)
    elif choice == "3":
      mark_task_completed(todo_list)
    elif choice == "4":
      delete_task(todo_list)
    elif choice == "5":
      print("Exiting the application. Goodbye!")
            break
        else:
print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()
