#1. Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class
class Circle():
    def __init__(self,radius):
        self.radius = radius
    def getArea(self):
        return 3.14 * self.radius*self.radius
    def getCircumference(self):
        return  2*3.14*self.radius
radius =int( input("enter radius"))
cir=Circle(radius)
print(cir.getArea())
#end


#2. Create a Student class and initialize it with name and roll number. Make methods to :
# Display - It should display all informations of the student
class Student:
    def __init__(self,rollno,age):
        self.rollno= rollno
        self.name= age
    def display(self):
        print(self.rollno)
        print(self.name)
roll=input("enter roll no")
name=input("enter name")
s= Student(display)
print(s.display())
#end


#3. Create a Temprature class. Make two methods :
###1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
###2. convertCelsius - It will take Fahrenheit and will convert it into Celsius
class Temperature():
    def  convertintoFahrenhiet(self,celsius):
        return (celsius * 9/5) + 32
    def convertintoCelsius(self,fahrenhiet):
        return (fahrenhiet - 32)*5/9
temp=Temperature()
c = temp.convertintoFahrenhiet(100)
f = temp.convertintoCelsius(98.4)
print(c,f)
#end


#4.Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to
##1. Display-Display the details.
##2. Update- Update the movie details
class MovieDetails:
    def __init__(self,name,artist,year,ratings):
        self.name=name
        self.artist=artist
        self.year=year
    def display(self):
        print("The",self.name,"of",self.artist,"has been released in",self.year)
    def update(self):
        name = input("Enter movie name: ")
        self.name = name
        artist = input("Enter artist name: ")
        self.artist = artist
        year = input("Enter year of release: ")
        self.year = year
        print("The",self.name,"of",self.artist,"has been released in",self.year)
movie=MovieDetails('race 3','salman khan',2018,16.6)
movie.display()
movie.update()
#end


#5.Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.
##1. Display expenditure and savings
##2. Calculate total salary
##3. Display salary
class Expenditure:
    def __init__(self,savings,expenditure):
        self.savings=savings
        self.expenditure=expenditure
    def display_expense(self):
        print(self.expenditure)
        print(self.savings)
    def cal_salary(self):
        total = self.savings + self.expenditure
        print("The total salary is",total)
savings = input("Enter savings: ")
expen = input("Enter expenditure: ")
exp = Expenditure(savings,expen)
exp.display_expense()
exp.cal_salary()
#end
