#tuples
#1. Creating a tuple
tup=('c','c++','python','java')
#printing tuples
print("The created tuples is",tup)
#printing the length of tuple
print("The length of the tuple is",len(tup))
#end


#2. creating a tuple
tup=(1,4,6,9,10,12)
print("The maximum element is",max(tup))
print("The minimum element is",min(tup))
#end


#3. creating a tuple product
tup=(1,4,6,9,10,12)
product=(1*4*6*9*10*12)
print("The product of the all the tuple elements is",product)
#end


#Sets
#1. Creating a set
days=set(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
values=set(['Monday','Sunday','Wednesday','Saturday'])
print("The first set is",days)
print("The first set is",values)
#end

#Difference of two sets
days=set(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
values=set(['Monday','Sunday','Wednesday','Saturday'])

#Displaying sets
print("The first set is",days)
print("The first set is",values)

#Difference between two sets
diff_set=days-values
print("The difference of two sets is",diff_set)

#Comparing two sets
days=set(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
values=set(['Monday','Sunday','Wednesday','Saturday'])
#Displaying sets
print("The first set is",days)
print("The first set is",values)

#Comparing two sets
res_set=days<=values
print("The result of the comparison of two sets is",res_set)


#Intersection of two sets
#Creating a set
days=set(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
values=set(['Monday','Sunday','Wednesday','Saturday'])
#Displaying sets
print("The first set is",days)
print("The first set is",values)

#Intersection of two sets
combined_set=days&values
print("The intersection of two sets is",combined_set)
#end



#Dictionaries
#1. Creating dictionaries
student={
'shubham':100,
'ankit':90,
'aman':75,
'naman':88,
'sudhanshu':65
}
#Displaying values
print("The marks dictionary is",student)
#end


2. #Sort the dictionary
student={
'shubham':100,
'ankit':90,
'aman':75,
'naman':88,
'sudhanshu':65
}
print("The marks dictionary is",student)
#end


#Sort the dictionary
for key in sorted(student):
   print("%s: %s" % (key, student[key]))
sorted(dict.keys())

#3.
s='MISSISSIPPI'
#converting string to lists
l=list(s)
m_count=l.count('M')
i_count=l.count('I')
s_count=l.count('S')
p_count=l.count('P')
#creating final dictionary
dict={
    'M':m_count,'I':i_count,'S':s_count,'P':p_count
}
print("The created dictionary is",dict)
#end
