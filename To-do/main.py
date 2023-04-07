from tkinter import *
from tkinter import messagebox

def newTask():
    task = myEntry.get()
    if task != "":
        lb.insert(END, task)
        myEntry.delete(0, "end")
    else:
        messagebox.showwarning('Warning', "Please enter some task")

def deleteTask():
    lb.delete(ANCHOR) # ANCHOR refers to the selected item in listbox.

ws = Tk()
ws.geometry('500x450+500+200') # width x height + x-position + y-position
ws.title('To-do List')
ws.config(bg='#223441')
ws.resizable(width = False, height = False)

# Frame
frame = Frame(ws)
frame.pack(pady = 10) # Padding

    #Listbox
lb = Listbox(
    frame,
    width = 25,
    height = 8,
    font = ('Times', 18),
    bd = 0, # Border
    fg = '#464646', # Foreground
    highlightthickness = 0, # every time the focus is moved to any item then it should not show any movement that is value 0 value is provided. by default it has some value.
    selectbackground = '#a6a6a6', # Decides the color of the focused item in the listbox
    activestyle = "none",
)

# Geometry Manager
lb.pack(side = LEFT, fill = BOTH) # Keeps ListBox on left side. 

        #TaskList
taskList = [

        # Daily Routine
    'Brush Teeth. -Morning',
    'Brush Teeth. -Afternoon',
    'Workout.',
    'Math Assignment',
    'Math Study',
    'take a nap',
    'Learn something',
    'paint canvas'
]

for item in taskList:
    lb.insert(END, item) # A new item will be added in the end. If END is replaced with 0 then new data will be added at the top.

sb = Scrollbar(frame)
sb.pack(side = RIGHT, fill = BOTH) # Assign Scrollbar to right side. 

lb.config(yscrollcommand = sb.set) # Assign purpose to Scrollbar.
sb.config(command = lb.yview) # Assign scrollbar to Y axis scrolling rather than X.

# Entry
myEntry = Entry(
    ws, # Entry placed in parent window. 
    font = ('Times', 24)
)

# Geometry Manager
myEntry.pack(pady = 20)

buttonFrame = Frame(ws) # Assign to Parent Window. 
buttonFrame.pack(pady = 20)

addTask_btn = Button(
    buttonFrame,
    text = 'Add Task',
    font = ('Times', 14),
    bg = '#ff8b61',
    padx = 20,
    pady = 10,
    command = newTask
)

addTask_btn.pack(fill = BOTH, expand = True, side = LEFT)

delTask_btn = Button(
    buttonFrame,
    text = 'Delete Task',
    font = ('Times', 14),
    bg = '#ff8b61',
    padx = 20,
    pady = 10,
    command = deleteTask
)

delTask_btn.pack(fill = BOTH, expand = True, side = LEFT)

# Main Loops
ws.mainloop()