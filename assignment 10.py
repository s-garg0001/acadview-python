#1. Create a class Animal as a base class and define method animal_attribute.
# Create another class Tiger which is inheriting Animal and access the base class method
class Animal():
    def Animal_attribute(self):
        print("lion")
class Tiger(Animal):
    print("cat")
t=Tiger()
t.Animal_attribute()
#end


#2. What will be the output of following code:
#print a.f(),b.f()=A,B



#3. Create a class Cop. Initialize its name, age , work experience and designation.
# Define methods to add, display and update the following details.
# Create another class Mission which extends the class Cop. Define method add_mission _details.
# Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission
class Cop():
    def __init__(self,name,age,workexperience,designation):
        self.n=name
        self.a=age
        self.w=workexperience
        self.d=designation
    def add(self):
        print("details are")
    def display(self):
        print("name=:" + self.n)
        print("age=:" + self.a)
        print("workexperience=:" + self.w)
        print("designation:" + self.d)
    def update(self,name,age,workexperience,designation):
        self.z=name
        self.x=age
        self.c=workexperience
        self.b=designation
        print("name=:"+self.z)
        print("age=:"+self.x)
        print("work=:"+self.c)
        print("designation:"+self.b)
class Mission(Cop):
    print("details are below:")
m=Mission("Shubham",str(20),"for indian army","with no experience","indian army")
m.add()
m.display()
m.update("Shubham",str(21),"for air force","7 missions","air force")
#end


#5. Create a class Shape.Initialize it with length and breadth Create the method Area.
# Create class rectangle and square which inherits shape and access the method Area
class Shape():
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
class Rectangle(Shape):
    def Area1(self):
        rectangle=self.l*self.b
        print(rectangle)
class Square(Rectangle):
    def Area2(self):
        square=self.l*4
        print(square )
s=Square(4,4)
s.Area1()
s.Area2()

