import tkinter
import urllib
import os
import sys
import json
import getpass as pwd

from Modules import mathfunc as math

password = pwd.getpass("password give now:")
if password == "Allah":
    print("ok")
else:
    sys.exit()
    

   
from urllib.request import urlopen

filepaths = []

x = math.deciwrite(10)

print(x)
    
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
            
            
          

for entry in os.scandir(r'D:\Abhinav\PyExecutor\Programs'):
    if entry.path.endswith('.py'):
        value = entry.path.replace(r'D:\Abhinav\PyExecutor\Programs', '')
        list.insert(0,value)
        filepaths.insert(0,entry.path)
        






list.pack()
executebutton = tkinter.Button(rootgui,text='Execute Program',command=selected)
executebutton.pack()

rootgui.wm_iconbitmap("D:/Abhinav/Textures/brickwall.png")
rootgui.geometry("300x200")
rootgui.mainloop() 
