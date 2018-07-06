#1. Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same
import pandas as pd
import numpy as np
d={'name':pd.Series(['shubham','aman','ankit','sudhanshu']),
   'age':pd.Series([20,19,20,15]),
   'mail':pd.Series(['skgarg390@gmail.com','amanaggarwal1998@gmail.com','bansalwwe@gmail.com@gmail.com','sudhanshusingla123@gmail.com']),
   'phoneno':pd.Series([9068204890,8950126596,8685868323,7082324890])}
df=pd.DataFrame(d,index=[1,2,3,4])
print(df)
print(df.axes)
print(df.dtypes)
print(df.shape)
print(df.values)
#end

#2.
df=pd.read_csv('question2-20.csv')
print(df.head(5))
print(df.head(10))
print("mean",df.mean)
print("describe",df.describe())
print(df.tail(10))
print("LOCATION")
print(df['Location'])
print(df['Location'].describe)
print("MINTEMP")
print(df['MinTemp'].describe())
print("Count ",df['MinTemp'].count())
print("Min ",df['MinTemp'].min())
print("Var ",df['MinTemp'].var())
print("Max ",df['MinTemp'].max())
print("Mean ",df['MinTemp'].mean())
print("Median ",df['MinTemp'].median())
print("Mode ",df['MinTemp'].mode())