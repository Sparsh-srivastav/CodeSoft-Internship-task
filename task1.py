'''
This project aims to develop a To-Do-List with a GUI  
'''
import tkinter 
from tkinter import *

root = Tk()
root.title("To-Do-list")
root.geometry("400x600+450+100")
root.resizable(False,True)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open('taskfile.txt','a') as taskfile:
            taskfile.write(f'\n{task}')
        task_list.append(task)
        listbox.insert(END, task)


def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('taskfile.txt','w') as taskfile:
            for task in task_list:
                taskfile.write(task+'\n')

        listbox.delete(ANCHOR)

        
def openTaskFile():
    try:
        global task_list
        with open('tasklist.txt','r') as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file = open('taskfile.txt','w')
        file.close()


# image
image_icon = PhotoImage(file='c:/Users/Sparsh/Desktop/Image/task.png')
root.iconphoto(False,image_icon)

# top bar
TopImage = PhotoImage(file='c:/Users/Sparsh/Desktop/Image/topbar.png')
Label(root,image=TopImage).pack()

dockImage = PhotoImage(file='c:/Users/Sparsh/Desktop/Image/dock.png')
Label(root,image=dockImage,bg='#32405b').place(x=30,y=25)

noteImage = PhotoImage(file='c:/Users/Sparsh/Desktop/Image/task.png')
Label(root,image=noteImage,bg='#32405b').place(x=30,y=25)

heading = Label(root,text='ALL TASK',font='arial 20 bold',fg='white',bg='#32405b')
heading.place(x=130,y=20)

# main
frame1 = Frame(root,width=400,height=50,bg='white')
frame1.place(x=0,y=180)

task = StringVar()
task_entry = Entry(frame1,width=18,font='arial 20',bd=5)
task_entry.place(x=10,y=7)
task_entry.focus()

button = Button(frame1,text='ADD',font='arial 20 bold',width=6,bg="#ff5e00",fg='#fff',bd=5,command=addTask)
button.place(x=300,y=0)

# list box 
frame2 = Button(root,bd=3,width=700,height=280,bg="#000000")
frame2.pack(pady=(160,0))

listbox = Listbox(frame2,font=('arial',12),width=40,height=16,bg="#221F1F",fg='white',cursor='hand2',selectbackground="#3E2E66")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scroll_bar = Scrollbar(frame2)
scroll_bar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=listbox.yview)

openTaskFile()

# delete
delete_icon = PhotoImage(file='c:/Users/Sparsh/Desktop/Image/delete.png') 
Button(root,image=delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)


root.mainloop()
