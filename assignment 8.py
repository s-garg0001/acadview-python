
#1. Many of Python's time functions handle time as a tuple
"representation of time in such a way that's make it easy to understand for us. Many of Python's time functions handle time as a tuple"
"index(0) field(day) value(1to30)"
"index(1) field(month) value(1to12)"
"index(2) field(year) value(2018)"
"index(3) field(hour) value(0to23)"
"index(4) field(minutes) value(0to59)"
"index(5) field(seconds) value(0to61)"
#end


#2. Write a program to get formatted time
import time
clock= time.localtime()
print(time.asctime())
#end


#3. Extract month from the time
from datetime import date
d=date.today()
print(d.month)
#end


#4. Extract day from the time
from datetime import date
d=date.today()
print(d.day)
#end


#5. Extract date (ex : 11 in 11/01/2021) from the time
import datetime
dt=datetime.date.today()
dt.strftime("%d%m%y")
print(dt.day)
#end


#6. Write a program to print time using localtime method
print(time.localtime())
#end


#7.Find the factorial of a number input by user using math package functions
import math
n=int(input("enter number"))
print(math.factorial(n))
#end


#8.  Find the GCD of a number input by user using math package functions
x=int(input("enter number"))
y=int(input("enter number"))
print(math.gcd(x,y))
#end


#9. Use OS package and do the following tasks:
# Get current working directory.
import os
print(os.getcwd())

# Get the user environment.
import os
print(os.environ)
#end