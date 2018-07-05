#1. #1Create a dict with name and mobile number.
# Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary
import tkinter as tk
from tkinter import *
skg=tk.Tk()
skg.title("info")
dict={'name':'shubham','mobile_number':9068204890}
scrollbar=Scrollbar(skg)
scrollbar.pack(side=LEFT,fill=Y)
mylist=Listbox(skg,yscrollcommand= scrollbar.set)
for key in dict.__iter__():
        mylist.insert(END,key)
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)
def skgarg():
    skg.quit()
b=Button(skg,text="enter",command=skgarg)
b.pack()
skg.mainloop()


#2.In the same tkinter file as created above, create a function to insert items into the dictionary
def shubham():
    dict.update({"age":21})
    print(dict)
button1=Button(skg,text='good',command=shubham)
skg.mainloop()
button1.pack()