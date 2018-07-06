#1. Create a numpy array with 10 elements of the shape(10,1)
# using np.random and find out the mean of the elements using basic numpy functions
import numpy as np
abc=np.random.random((10,1))
print(abc)
print("Mean of 10 random no. :",abc.mean())
print("Mean of 10 random no. :",np.mean(abc))
#end


#2. reate a numpy array with 20 elements of the shape(20,1) using np.random find the variance and standard deviation of the elements
a=np.random.rand(20,1)
print(a)
print("Variance :", a.var())
print("Standard Deviation :",a.std())
#end


#3. Create a numpy array A of shape(10,20) and B of shape (20,25) using np.random.
#  Print the matrix which is the matrix multiplication of A and B.
#  The shape of the new matrix should be (10,25). Using basic numpy math functions only find the sum of all the elements of the new matrix
A=np.random.random((10,20))
B=np.random.random((20,25))
C=np.dot(A,B)
print("Matrix",C)
print("Shape",C.shape)
print("Sum",np.sum(C))
#end


#4. Create a numpy array A of shape(10,1).Using the basic operations of the numpy array generate an array of shape(10,1)
# such that each element is the following function applied on each element of A
from math import exp
def skg(k):
    return (1/(1+(np.exp(-k))))
A=np.random.rand(10,1)
print("OLD array :",A)
B=skg(A)
print("NEW array :",B)
#end