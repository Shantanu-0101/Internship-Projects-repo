import json
import csv

def save_to_json(tasks, filename="tasks.json"):
    with open(filename, 'w') as file:
        json.dump(tasks, file)
    print(f"Tasks saved to {filename}")

def save_to_csv(tasks, filename="tasks.csv"):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task])
    print(f"Tasks saved to {filename}")
    
def tasks():
    tasks = []
    print("welcome to task manager")

    try:
        num_tasks = int(input("Enter How many tasks you want to add :"))
    except ValueError:
        print("Invalid Input Pls Enter an integer:")
        return
    
    for i in range (1, num_tasks + 1):
        task_name = input(f'Enter task {i} :')
        tasks.append(task_name)

    print(f'Your tasks are\n{tasks}')

    while True:
         operation = input("enter 1 - add\nenter 2 - update\nenter 3 - view\nenter 4 - delete\nenter 5 - exit\n6 - Save to JSON\n"
            "7 - Save to CSV\n")

         if operation == '1':
             add = input("Enter to Add new task:")
             tasks.append(add)
             print(f'task added successfully {add}')
             print(f'Your tasks are {tasks}')

         elif operation == '2':
             update = input("Enter which task you want to update:")
             task_found = False
             for index, task in enumerate(tasks):
                 if update.lower() == task.lower():
                     task_found = True
                     up = input("enter new task:")
                     tasks[index] = up
                     print(f'task updated successfully {up}')
                     break
             if not task_found:
                     print("Task not found")

         elif operation == '3':
             if tasks:
                 print("your tasks are:")
                 for i, task in enumerate(tasks,1):
                     print(f'{i} {task}')
             else:
                 print("No tasks to show")

         elif operation == '4':
             del_task = input("Enter which task to delete:")
             task_found = False
             for task in tasks:
                 if del_task.lower() == task.lower():
                     task_found = True
                     tasks.remove(del_task) 
                     print(f"Your task successfully deleted {del_task}")
                     break
             if not task_found:
                     print("task not found")

         elif operation == '5':
             print("exitig Task manager")
             break
         
         elif operation == '6':
            save_to_json(tasks)

         elif operation == '7':
            save_to_csv(tasks)
         
         else:
             print("invalid input pls enter a valid input")

if __name__ == "__main__":
    tasks()       
