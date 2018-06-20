#1. Create a function to calculate the area of a circle by taking radius from user
radius=float(input("enter no."))
def area(rad):
    area=3.14*rad*rad
    return area
ar=area(radius)
print(ar)
#end


#2. Write a function “perfect()” that determines if parameter number is a perfect number.
#  Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
#[An integer number is said to be “perfect number” if its factors,
#including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3]
def perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
    if (sum == n):
        return True
    else:
        return False
for i in range(1, 1001):
    if perfect(i):
        print(i)
#end


#3. Print multiplication table of 12 using recursion.
def table(m,i):
  print (m*i)
  i=i+1
  if (i<=10):
    table(m,i)
table(14,1)
#end


#4. Write a function to calculate power of a number raised to other ( a^b ) using recursion
def power(a,b):
    if(b==1):
        return a
    else:
        return a*power(a,b-1)
print(power(6,2))
#end

#5.
# Python program to find the factorial of a number provided by the user.
num = 6
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
