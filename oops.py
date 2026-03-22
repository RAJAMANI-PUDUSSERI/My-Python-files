# class variables

class Student:
    class_year = 2025 #class varible defined outside the constructor
    number_of_students = 0

    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age
        Student.number_of_students +=1

# student1 = Student("Sponge Bob", 20)
# student2 = Student("Patrick", 25)
# student3 = Student("Caroline", 22)
# student4 = Student("Luca", 18)

# print(f"In the year {Student.class_year} there are {Student.number_of_students} students and the following is the list:")
# print(f"1.{student1.name} aged {student1.age}")
# print(f"2.{student2.name} aged {student2.age}")
# print(f"3.{student3.name} aged {student3.age}")
# print(f"4.{student4.name} aged {student4.age}")


# inheritance is
# inheritance examle
class Animals:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age
        self.is_alive:bool = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animals):
    def describe(self):
        print(f"{self.name} is {self.age} old and is alive = {self.is_alive}")
    
    def speak(self):
        print(f"{self.name} is BARKING")

class Cat(Animals):
    def describe(self):
        # print(f"{self.name} is {self.age} old and is alive = {self.is_alive}")
        return f"{self.name} is {self.age} old and is alive = {self.is_alive}"
    def speak(self):
        print(f"{self.name} is MEWOING")

class Mouse(Animals):
    def describe(self):
        print(f"{self.name} is {self.age} old and is alive = {self.is_alive}")

    def speak(self):
        print(f"{self.name} is SQEEKING")

class Cars: #Duck typing
    def __init__(self,is_alive:bool):
        self.is_alive = is_alive

    def speak(self): #Car honks similar to animal speak, If it looks like and quaks like a duck it must be a duck.
        return "the Car is HONKING"

    def describe(self):
        print(f"The car is {'alive' if self.is_alive else 'not alive'} and {self.speak()}")

dog1 = Dog("Scooby", 5)
cat1 = Cat("Garfield", 6)
mouse1 = Mouse("Mickey", 3)
car1 = Cars(False)

# dog1.describe()
# dog1.eat()
# cat1.describe()
# cat1.speak()  
# mouse1.describe()
# mouse1.sleep()
# car1.describe()

# multiple and multi inheritance
class Animal:
    def __init__(self, name:str) -> None:
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        return f"is fleeing"

class Predator(Animal):
    def hunt(self):
        return f"is hunting"

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bunny")
hawk = Hawk("Tony")
fish = Fish("Nemo")

# rabbit.eat()
# hawk.sleep()
# print(f"{fish.name} is {fish.flee()} and also {fish.hunt()}")

# Abstract class
# abstract classes example
from abc import ABC, abstractmethod

class Vehicle:
    @abstractmethod
    def go(self):
        pass
    def stop(self):
        pass

class Limousine(Vehicle):
    def go(self):
        print("This limousine is driving")
    def stop(self):
        print("This car limousine stopping")

class Motorcycle(Vehicle):
    def go(self):
        print("This motorcycle is riding")
    def stop(self):
        print("This motorcycle is stopping")

limousine = Limousine()
motorcycle = Motorcycle()

# limousine.go()
# motorcycle.go()
# motorcycle.stop()

# super()
# super() examples

class Shapes: 
    def __init__ (self, color:str, is_filled:bool):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"is {self.color} in color and {"is filled" if self.is_filled else "not filled."}")

class Circles(Shapes):
    def __init__ (self, color:str, is_filled:bool, radius:float):
        super().__init__(color,is_filled)
        self.radius = radius

    def describe(self):
        print(f"This circle has an area of {3.14*self.radius**2}cm^2, and", end=' ')
        super().describe()

class Squares(Shapes):
    def __init__(self,color:str,is_filled:bool,width:float):
        super().__init__(color,is_filled)
        self.width = width
    
    def describe(self):
        print(f"This square has an area of {self.width**2}cm^2, and", end=' ')
        super().describe()

class Rectangles(Shapes):
    def __init__(self,color:str,is_filled:bool,width:float,height:float):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"This rectangle has an area of {self.width*self.height}cm^2, and", end=' ')
        super().describe()

class Triangles(Shapes):
    def __init__(self,color:str,is_filled:bool,width:float,height:float):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"This triangle has an area of {(self.width*self.height)/2}cm^2", end=' ')
        super().describe()

circle_new = Circles("red", True, 1.5)
square_new = Squares("white", False, 2.0)
rectangle_new = Rectangles("blue",False, 2.0, 1.5)
triangle_new = Triangles("yellow",True, 2.0, 1.5)

# circle_new.describe()
# square_new.describe()
# rectangle_new.describe()
# triangle_new.describe()

# Polymorphism is a fundamental concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying data types, allowing for flexibility and extensibility in code design. In Python, polymorphism can be achieved through method overriding and duck typing.

class Shape:
    """Base class for all shapes"""
    def __init__(self, name : str, color : str | None = None, is_filled: bool = False): # Initialize the shape with a name, color, and filled status
        self.name = name
        self.color = color
        self.is_filled = is_filled

    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def describe(self) -> str:
        return f"{self.name} is {self.color} in color and is filled {self.is_filled}"
    
class Circle(Shape):
    def __init__(self, radius: float,color: str | None=None,is_filled=False):
        super().__init__("Circle",color,is_filled) # Call the Shape constructor to initialize the name
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(Shape): 
    def __init__(self, width: float, height: float,color :str | None=None,is_filled:bool=False):
        super().__init__("Rectangle",color,is_filled) # Call the Shape constructor to initialize the name
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height
    
class Triangle(Shape):
    def __init__(self, base, height,color: str | None=None,is_filled=False):
        super().__init__("Triangle",color,is_filled) # Call the Shape constructor to initialize the name
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
class Pizza(Circle):
    def __init__(self, topping,radius):
        super().__init__(radius) # Call the Circle constructor to initialize the radius
        self.topping = topping
        self.name = f"Pizza with {self.topping}"

    # def area(self):
    #     return 3.14 * self.radius ** 2
    
    def describe(self):
        return f"{self.name} is a delicious pizza with {self.topping} topping and has a radius of {self.radius}cm"
    
shapes = [Circle(radius=5,color="red",is_filled=True), Rectangle(width=4, height=6,color="blue",is_filled=False), Triangle(base=3, height=4,color="green",is_filled=True), Pizza(topping="pepperoni", radius=7)]
# for shape in shapes:
#     print(f"The  {shape.describe()}, has the area of:{shape.area()}cm^2")
    # print(f"The Color of the {shape.name} is: {shape.color}, Filled: {shape.is_filled}")

# Duck typing is a programming style in Python that emphasizes the use of objects based on their behavior rather than their specific type. It allows for more flexible and dynamic code, as it does not require strict type checking. In duck typing, if an object behaves like a certain type (i.e., it has the necessary methods and properties), it can be used as that type, regardless of its actual class.
# Duck typing example
def describe_shape(shape):
    print(shape.describe())
# describe_shape(Circle(radius=5,color="red",is_filled=True))
# describe_shape(Rectangle(width=4, height=6,color="blue",is_filled=False))
# describe_shape(Triangle(base=3, height=4,color="green",is_filled=True))
# describe_shape(Pizza(topping="pepperoni", radius=7))


# Aggregation is a design principle in object-oriented programming where one class contains a reference to another class, allowing for a "has-a" relationship. It is a way to model relationships between classes without creating a strong dependency between them. In aggregation, the contained class can exist independently of the container class, meaning that if the container class is destroyed, the contained class can still exist.
# Aggregation example
class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = [] # Initialize an empty list to hold books

    def add_book(self, book: str):
        self.books.append(book) # Add a book to the library's collection

    def list_books(self):
        return f"{self.name} has the following books: {', '.join(self.books)}"
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        
    def describe(self):
        return f"{self.title} by {self.author}"
# Create a library and add books to it
my_library = Library("City Library")
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")
my_library.add_book(book1.describe())
my_library.add_book(book2.describe())
# print(my_library.list_books())

# Composition is a design principle in object-oriented programming where one class contains an instance of another class, creating a strong "has-a" relationship. In composition, the contained class cannot exist independently of the container class, meaning that if the container class is destroyed, the contained class will also be destroyed.
# Composition example
class Car:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        self.engine = Engine() # Create an instance of the Engine class as part of the Car

    def describe(self):
        return f"{self.make} {self.model} with {self.engine.describe()}"
class Engine:
    def describe(self):
        return "a powerful engine"
# Create a car and describe it
my_car = Car("Toyota", "Camry")
# print(my_car.describe())

# Nested classes = A class defined within another class
# Nested classes examples

class Company:
    class Employee:
        def __init__(self, name:str, position:str):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} the {self.position}"
        
        @staticmethod
        def is_valid_position(position): #static methods, which belongs to the class and not to the instance, used in general utility
            valid_positions = ["Manager", "Clerk","Assistant","Cashier","Cook","Accountant"]
            return position in valid_positions 
    
    # print(Employee.is_valid_position("Rocket Sceintist"))    #call the static method
    
    def __init__(self, company_name:str):
        self.company_name = company_name
        self.employees = []
 
    def add_employee(self, name:str, position:str):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]
    
company1 = Company("Krusty Krab")
company2 = Company("Chum Bucket")

company1.add_employee("Eugene", "Manager") #instance methods
company1.add_employee("Spungebob", "Cook")
company1.add_employee("Squidward", "Cashier")

company2.add_employee("Sheldon", "Manager")
company2.add_employee("Karen", "Assistant")
company2.add_employee("Cooper", "Accountant")

# for employee in company1.list_employees():
#    print (f"{employee} is working in {company1.company_name}")
# print(company1.list_employees())  # call the instance method
# print(company2.list_employees())    
# for employee in company2.list_employees():
#     print (f"{employee} is working in {company2.company_name}")

# class methods = allow operations relating to the class itself
class Students:
    
    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Students.count += 1
        Students.total_gpa += gpa

    #Instance method
    def get_info(self):
        return f"{self.name} has scored {self.gpa} GPA"
    
    #Class method
    @classmethod
    def get_count(cls):
        return f"Total number of students = {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA = {cls.total_gpa / cls.count:.2f}"
        
    
    
student1 = Students("Eugene", 3.0)
student2 = Students("Caroline", 2.0)
student3 = Students("Sandy", 4.0)
student1 = Students("Patric", 2.5)

# print(student1.get_info()) #calling the Instance method
# print(Students.get_count()) #calling the Class method
# print(Students.get_average_gpa())

class Geeks:
    
    course = "DSA"
    instances = []

    def __init__(self,name:str):
        self.name = name
        Geeks.instances.append(self)

    @classmethod
    def get_course(cls):
        return f"Course : {Geeks.course}"
    
    @classmethod
    def get_instances(cls):
        return f"No of Geeks : {len(Geeks.instances)}"
    
geek1 = Geeks("Patric")
geek2 = Geeks("Sandy")
geek1 = Geeks("Carol")

# print(Geeks.get_course())
# print(Geeks.get_instances())

class Staff:
    bank_name = "SBI"

    def __init__(self,name:str,salary:int):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls,staff_str:str):
        """Factory method to create staff and salary from string.
           Example string "Patrick-5000" """
        try:
            name,salary = staff_str.split('-')
            return cls (name, int(salary)) 
            
        except ValueError:
            raise ValueError("Invalid emp_str : use 'Name-Salary'.")
        
    @classmethod
    def change_bank_name(cls,new_bank_name:str):
        """Change the Bank Name for all Staff"""
        cls.bank_name = new_bank_name

# using class method as a factory
staff1 = Staff.from_string("Alice-7000")
# print(staff1.name,staff1.salary,staff1.bank_name)

Staff.change_bank_name("CBI")
# print(staff1.bank_name)

from datetime import date
class Person:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls,name,birth_year):
        return cls(name, date.today().year - birth_year)
    
person1 = Person.from_birth_year("Alex",1955)
# print(person1.name, person1.age) # search @classmethods in web geeksforgeeks, w3schools, programz

class Date:
    def __init__(self,date,month,year):
        self.date = date
        self.month = month
        self.year = year

    @classmethod
    def from_date_str(cls,date_string):
        date,month,year = map(int, (date_string.split('-'))) #The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.here int is a function
        return cls(date,month,year)
    # Here, from_date_string is a factory method that creates an instance of the Date class from a string:
date1 = Date.from_date_str("15-03-2026")
# print(date1.date,date1.month,date1.year)

class ThreeDpoint:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_sequence(cls,sequence):
        return cls(*sequence)
    def __repr__(self) -> str:
        return f"(x={self.x},y={self.y},z={self.z})"
    
sequence = ThreeDpoint.from_sequence((4,6,8))
# print(sequence)

# from typing import Self # for anotation purpose only
# class Auto:
#     total_cars:int = 0

#     def __init__(self, brand:str, top_speed:int) -> None:
#         self.brand = brand
#         self.top_speed = top_speed
#         Auto.total_cars +=1

#     @classmethod
#     def auto_top_speed(cls,brand:str) -> Self:
#         database:dict[str,int] =  {"bmw" : 250, "volvo" : 200, "audi" : 225}
#         top_speed: int | None = database.get(brand.lower())

#         if top_speed:
#             print(f"Set top speed to : {top_speed}")

#         else:
#             print(f"Could not find {brand} , so setting default to 150")
#             top_speed = 150

#         return cls(brand=brand,top_speed=top_speed)
    
#     @classmethod
#     def total_cars_created(cls) -> int:
#         return Auto.total_cars

#     def __str__(self) -> str:
#         return f"{self.brand} {self.top_speed} km/h"

# bmw : Auto = Auto.auto_top_speed("BMW")
# print(bmw)
# print(Auto.total_cars_created())
# volvo : Auto = Auto.auto_top_speed("VOLVO")
# print(volvo)
# print(Auto.total_cars_created())
# audi : Auto = Auto.auto_top_speed("AUDI")
# print(audi)
# print(Auto.total_cars_created())
# mercedes : Auto = Auto.auto_top_speed("MERCEDES")
# print(mercedes)
# print(Auto.total_cars_created())

# Alternate better code previous one commented for future ref

from typing import Self # for anotation purpose only
class Auto:
    total_cars:int = 0

    def __init__(self, brand:str, top_speed:int) -> None:
        self.brand = brand
        self.top_speed = top_speed
        Auto.total_cars +=1

    @classmethod
    def auto_top_speed(cls,brand:str) -> Self:
        database:dict[str,int] =  {"bmw" : 250, "volvo" : 200, "audi" : 225}
        top_speed: int | None = database.get(brand.lower())

        if not top_speed:
            print(f"Could not find {brand} , so setting default to 150")
            top_speed = 150
        return cls(brand=brand,top_speed=top_speed)
    
    @classmethod
    def total_cars_created(cls) -> int:
        return Auto.total_cars

    def __str__(self) -> str:
        return f"{self.brand} {self.top_speed} km/h"

# bmw : Auto = Auto.auto_top_speed("BMW")
# print(Auto.total_cars_created())
# print(bmw)
# volvo : Auto = Auto.auto_top_speed("VOLVO")
# print(Auto.total_cars_created())
# print(volvo)
# audi : Auto = Auto.auto_top_speed("AUDI")
# print(Auto.total_cars_created())
# print(audi)
# mercedes : Auto = Auto.auto_top_speed("MERCEDES")
# print(Auto.total_cars_created())
# print(mercedes)
# Magic methods 
class Novel:
    def __init__(self,name:str,author:str,num_pages:int):
        self.name = name
        self.author = author
        self.num_pages = num_pages

    def __str__(self): # retun string representation of the object
        return f"'{self.name}'by {self.author}"
    
    def __eq__(self, other) -> bool:
        return self.name == other.name and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.name or keyword in self.author
    
    def __getitem__(self, key):
        if key == "name":
            return self.name
        elif key == "author":
            return self.author
        elif key== "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' not found"

novel1 = Novel("To Kill a Mockingbird", "Harper Lee", 250)
novel2 = Novel("1984", "George Orwell", 275)
# print(novel1)
# print(novel1 == novel2)
# print(novel1 < novel2)
# print(novel1 > novel2)
# print(novel1 + novel2)
# print('Kill' in novel1)
# print('George' in novel2)
# print(novel1["name"])
# print(novel2["author"])
# print(novel1["num_pages"])
# print(novel1["audio"])

# Property decorator
class Polygon:
    def __init__(self,side_size:int,number_of_sides:int):
        self._side_size = side_size #private object
        self._number_of_sides = number_of_sides

    @property
    def side_size(self):
        return f"{self._side_size:.1f}"
    @property
    def number_of_sides(self):
        return f"{self._number_of_sides}"
    
    @number_of_sides.setter
    def number_of_sides(self,new_number_of_sides):
        if new_number_of_sides > 0:
            self._number_of_sides = new_number_of_sides
        else:
            print("Number of sides must be greater than zero")

    @side_size.setter
    def side_size(self,new_side_size):
        if new_side_size > 0:
            self._side_size = new_side_size
        else:
            print("Side Size must be greater than zero")
    
    @number_of_sides.deleter
    def number_of_sides(self):
        del self._number_of_sides
        print("Number of sides has been deleted")

    @side_size.deleter
    def side_size(self):
        del self._side_size
        print("Side size has been deleted")

polygon1 = Polygon(6,8)

# polygon1.number_of_sides = 0 # Number of sides must be greater than zero
# polygon1.number_of_sides = 10
# polygon1.side_size = -1 # Side Size must be greater than zero
# polygon1.side_size = 8
# print(polygon1._side_size)
# print(polygon1._number_of_sides)
# print(polygon1.side_size)
# print(polygon1.number_of_sides)
# del polygon1.number_of_sides
# del polygon1.side_size