#1.Take 10 integers from user and print it on screen
i =(10)
a = []
while(i<11):
  print ("Enter number")
  num = input()
  a.append(num)
  i = i+1
print (a)
#end

#2. Write an infinite loop.An infinite loop never ends. Condition is always true
while(True):
    print("hello")
#end

#3.  Create a list of integer elements by user input.
# Make a new list which will store square of elements of previous list
l=[]
k=[]
for i in range(1,5):
    c=int(input("enter number"))
    l.append(c)
    k.append(c*c)
print(l)
print(k)
#end


#4. From a list containing ints, strings and floats,
#  make three lists to store them separately
s=[1,"aman",3.5,2,5,"hello",2.4,2.6,"hey"]
p=[]
q=[]
r=[]
for i in s:
    if(isinstance(i,int)):
        p.append(i)
    elif (isinstance(i,str)):
        q.append(i)
    else:
        r.append(i)
print("list: ",s)
print("Integer: ", p)
print("String: ", q)
print("Float: ", r)
#end


#5. Using range(1,101), make a list containing even and odd numbers
even=[]
odd=[]
for I in range(1,101):
    if(I%2==0):
        even.append(I)
    else:
        odd.append(I)
print("The even list",even)
print("The odd list",odd)
#end


#6. Print the following patterns:
#*
#**
#***
#****
for I in range(0,4):
    for I in range(0,I+1):
        print("*",end="")
    print()
#end


#7.  Create a user defined dictionary and get keys corresponding to
# the value using for loop
D={'k': 20,
   'r': 30}
for key in D:
    print(key,D[key])
#end


#8. Take inputs from user to make a list.
# Again take one input from user and search it in the list and delete that element,
#  if found. Iterate over list using for loop
e=['shubham','aman','ankit','sahil','naman']
f=input("enter name")
for i in e:
    if i==f:
        e.remove(i)
        print(e)