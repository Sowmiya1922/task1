

tasks = []
def add_task(description):
    task ={"description":description, "completed": False}
    tasks.append(task)
    print("the task was added successfully!!")

def view_task():
    if not tasks:
        print("these task was not available")
        return
    
    for index, task in enumerate(tasks):
        status= "completed" if task["completed"] else "pending"
        print(f"{index + 1}. {task['description']} - {status}")


    

def completed_task(task_num):
    if task_num <=0 or task_num >len(tasks):
        print("these task number is invalid")
    else:
        tasks[task_num - 1]["completed"]=True
        print(len(tasks),"task as completed")


while True:
    print("&&& MENU LIST FOR TO-DO APP &&&")
    print("1.Addig a Task")
    print("2.Viewing a Task")
    print("3.Completed the Task")
    print("4.Exit the TO DO LIST")


    choice = input("enter your choice:  ")

    if choice == "1":
        description1= input("Enter the Task Description:  ")
        add_task(description1)

    elif choice =="2":
        view_task()

    elif choice =="3":
        num = int (input("Enter task number to complete: "))
        completed_task(num)

    elif choice =="4":
        print("Existing the TO-DO APP")
        break

    else:
        print("Invalid choices" )