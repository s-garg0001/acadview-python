
#1. Create a list with user defined inputs.
a=input("enter integer value")
b=input("enter float value")
c=input("enter complex value")
l=[]
l.append(a)
l.append(b)
l.append(c)
print(l)
#end



#2. Add the following list to above created list:
i=["google","apple","facebook","microsoft","tesla"]
l.append(i)
print(l)
#end



#3. Count the number of time an object occurs in a list. queation3
j=[2,3,4,5,6,2,8]
print(j.count(2))
#end

#4. create a list with number and sort it in ascending order
j.sort()
print(j)
#end



#5. Given are two one-dimensional arrays A and B which are sorted in ascending order.
# Write a program to merge them into a single sorted array C that contains
#  every item from arrays A and B, in ascending order. [List]
p=[1,3,5,7,9]
q=[2,4,6,8,10]
r=(p+q)
r.sort()
print(r)
#end



#6. Implement a stack and queue using lists.
k=[1,"shubham","sgarg",39]
k.pop(1)
print(k)
k.insert(1,"my name is ")
print(k)
print("adding 10")
k.append(10)
print(k)
#end



#Optional.  Count even and odd numbers in that list.
x={1,2,3,4,5,6,7,8,9,10}
odd=0
even=0
for y in x:
        if not (y % 2):
    	     even=even+1
        else:
    	     odd=odd+1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)
#end