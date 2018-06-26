#1. Create a threading process such that it sleeps for 5 seconds and then prints out a message
import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def _init_(self):
        threading.Thread._init_(self)
    def run(self):
        time.sleep(5)
        print("Value after 5seconds")
th = mythread()
th.start()
#end


#2. Make a thread that prints numbers from 1-10, waits for 1 sec between
class mythread1(threading.Thread):
    def _init_(self):
        threading.Thread._init_(self)
    def run(self):
        for i in range(1, 11):
            time.sleep(1)
            print(i)
thr = mythread1()
thr.start()
#end


#3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of
# the list with a delay of multiple of 2 sec between each display.
#Delay goes like 2sec-4sec-6sec-8sec-10sec
import threading
import time
class Mythread(threading.Thread):
    def __init__(self,value):
        threading.Thread.__init__(self)
        self.v=value
    def run(self):
        a=(2,4,6,8,10)
        for i in range (0,5):
            print(self.v[i])
            time.sleep(a[i])
thread1=Mythread([1,2,3,4,5])
thread1.start()
#end


#4. Call factorial function using thread
import time
import threading
import math
class Mythread1 (threading.Thread):
    def __init__(self,a):
        threading.Thread.__init__(self)
        self.a=a
    def run(self):
            print("factorial of %d= %d"%(self.a, math.factorial(self.a)))
a=int(input("enter number"))
TT=Mythread(a)
TT.start()
#end