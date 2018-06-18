#1. leap year by user defined input
a=int(input("enter year"))
if(a%4==0):
    print("leap year")
else:
    print("not a leap year")
#end


#2. Take length and breadth input from user and check whether the dimensions are of square or rectangle.
l=int(input("enter length"))
b=int(input("enter breadth"))
if(l==b):
    print("it is square")
else:
    print("it is a rectangle")


#3. take input age of 3 people and determine older and younger among them
p=input("enter age 1")
q=input("enter age 2")
r=input("enter age 3")
if(p>q):
    if(p>r):
        print("p is older")
    else:
        print("r is older")
elif(q<r and q<p):
    print("q is younger")
elif(r<q and r<p):
    print("r is younger")
elif(q>p and q>r):
    print("q is older")
else:
    if(p<r):
        print("p is younger")
#end

#4. question ....
print("Enter points")
points=int(input(""))
if(points<51):
  print ("Sorry! No prize this time")
elif (points>=51 and points<=150):
  print("Congratulations! You won a wooden dog!")
elif (points>=151 and points<181):
  print("Congratulations! You won a book!")
elif (points>=181 and points<=200):
  print("Congratulations! You won a chocolate!")
#end

#5. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity Suppose, one unit will cost 100.
#  Judge and print total cost for user.
x=int(input("enter quantity"))
x=x*100
if(x>1000):
    x=x*100-x*.1*100
print(x)
