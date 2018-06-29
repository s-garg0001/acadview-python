#1. Name and handle the exception occured in the following program
a=3
if a<4:
    a=a/(a-3)
    print(a)
#ZeroDivisionError
#end


#2. Name and handle the exception occurred in the following program:
#l=[1,2,3]
#print(l[3])
l=[1,2,3]
print(l[3])
#IndexError
#end


#3. What will be the output of the following code:
class NameError(Exception):
    pass
try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
#an Exception will print
#end


#4. What will be the output of the following code
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
#-5.0
#a/b result in 0 will print
#end


#5. Write a program to show and handle following exceptions:
##1. Import Error
##2. Value Error
##3. Index Error
try:
    import yourname
    a=[1,2,3,4]
    print(a[4])
except ZeroDivisionError:
    print("no. is divided by zero")
except IndexError:
    print("index does not exist")
except ImportError:
    print("import file does not exit")
#end


#6. Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
# The code must keep taking input till the user enters the appropriate age number(less than 18)
class AgeTooSmallError(Exception):
    pass
try:
    a=int(input("enter age"))
    if(a<18):
        raise AgeTooSmallError
        print("nott matched")
except ValueError:
    print("please enter int value")
else:
    print("matched")
finally:
    print("thankyou")
#end