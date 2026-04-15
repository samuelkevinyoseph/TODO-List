#To Do list
tasks=[]

while True:
  print("1.Add new task")
  print("2.View task")
  print("3.Remove task")
  print("4.Exit")

  choice=int(input("Enter choice: "))


  if choice==1:
    task=input("Enter task: ")
    tasks.append(task)
    print("Task added")

  elif choice==2:
    print(tasks)

  elif choice==3:
    print(tasks)
    a=int(input("What task to remove? "))
    tasks.pop(a-1)
    print("Task removed")

  else:
    break


