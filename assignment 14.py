#1. Write a Python program to read last n lines of a file
f = open("test.txt", "r")
print(f)
for line in reversed(list(open("test.txt", "r"))):
    print(line.rstrip())
print(f.readlines())
n = input("Enter number of last lines ")
f = open("test.txt")
lines=f.readlines()
print("Last lines :", lines[0:n-1])
#end


#2. Write a Python program to count the frequency of words in a file
import re
import string
word=input("enter word ")
fear=0
with open("test.txt",'r',encoding="utf8") as f:
    for line in f:
        words=line.split()
        for i in words:
            if(i==word):
                fear=fear+1
print("no. of times the word appeared :",fear)
#end


#3.Write a Python program to copy the contents of a file to another file
with open("test.txt","r") as f:
    with open("paper.txt", "w") as f1:
        f1.write("S_GARG0001")
        for line in f:
            f1.write(line)
#end


#4.Write a Python program to combine each line from first file with the corresponding line in second file
'''with open(“test.txt”,"r") as fh1, open(“paper.txt”."r") as fh2:
    for l1, l2 in zip(fh1, fh2):
    print(l1 + l2)'''
#end


#5. Write a Python program to write 10 random numbers into a file.
#  Read the file and then sort the numbers and then store it to another file
import random
with open("random.txt", "w") as f:
    for i in range(int(input('random numbers'))):
        line = str(random.randint(1, 100))
        f.writelines(line +'\n')
        print(line)
with open("random.txt") as f1, open("random1.txt", "w") as f2:
    lines = f1.read().splitlines()
lines.sort()
for l in lines:
    f2.write(str(l) + '\n')
#end
