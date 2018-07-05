#1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface
import tkinter as tk
def destroy():
    m.destroy()
m=tk.Tk()
m.title("skg")
var = StringVar()
label= Label(m,textvariable=var)
var.set("hello world")
button=tk.Button(m,text='exit',width=25,command=destroy)
label.pack()
button.pack()
m.mainloop()
#end


#2. Write a python program to in the same interface as above and
# create a action when the button is click it will display some text
from tkinter import *
def func():
    print("Button clicked...")
widget = Button(None,text="Hello GUI World",command=func)
widget.pack(side=BOTTOM,expand = YES,fill=Y)
#end



#3. Create a frame using tkinter with any label text and two buttons.
# One to exit and other to change the label to some other text
from tkinter import *
import tkinter as tk
s=tk.Tk()
s.title("skgarg")
def mo():
    s.destroy()
button1=tk.Button(s,text='exit',width=25,command=mo)
button1.pack()
def moh():
    var1 = StringVar()
    label1 = Label(s, textvariable=var1)
    var1.set("my name is shubham")
    label1.pack()
    label2.destroy()
button2=tk.Button(s,text='name',command=moh)
button2.pack()
var2 = StringVar()
label2 = Label(s, textvariable=var2)
var2.set("my name is skg")
label2.pack()
s.mainloop()
#end


#4. Write a python program using tkinter interface to take an input in the GUI program and print it
from tkinter import *
fr = Frame()
fr.pack()
ent = Entry(fr)
ent.pack(side=TOP)
ent.insert(0,"type here...")
#ent.config(state='disabled')
ent.focus()
def display():
    print("This is the input:",ent.get())
widget = Button(fr,text="Hello GUI World",command=display)
widget.pack(side=LEFT,expand=YES,fill=Y)
widget.mainloop()
#end
