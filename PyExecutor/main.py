import tkinter
import os
import sys

    
rootgui = tkinter.Tk()
rootgui.title('PyExecutor')
list = tkinter.Listbox(rootgui, selectmode='SINGLE')

def selected():
    ActivVal = str(list.get(list.curselection()))
    for i in filepaths:
        if i.find(ActivVal) != -1:
            with open(i,"rb") as file:
                print("-----------")
                exe = compile(file.read(),str(i),"exec")
                exec(exe)
            
            
          

for entry in os.scandir(r'ENTER THE PATH FOR PROGRAMS FOLDER HERE'):
    if entry.path.endswith('.py'):
        value = entry.path.replace(r'ENTER THE PATH FOR PROGRAMS FOLDER HERE', '')
        list.insert(0,value)
        filepaths.insert(0,entry.path)
        



list.pack()
executebutton = tkinter.Button(rootgui,text='Execute Program',command=selected)
executebutton.pack()

rootgui.geometry("300x200")
rootgui.mainloop() 
