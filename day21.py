#Hey guys , Today we are going to learn Classes and Objects

#Python is an object oriented programming language. Everything in Python is an object, 
# with its properties and methods. A number, string, list, dictionary, tuple, set etc. used in a program is an object of a corresponding built-in class. 

#Creating a class
#syntax
#class Classname:
    #code goes here

#example
class Person:
    pass
print(Person) #<class '__main__.Person'>

#Creating an object (calling the class
p = Person()
print(p)

#Class Constructor
#In the examples above, we have created an object from the Person class.
#  However, a class without a constructor is not really useful in real applications. 
# Let us use constructor function to make our class more useful. Like the constructor function in Java or JavaScript,
#  Python has also a built-in init() constructor function. The init constructor function has self parameter which is a reference to the current instance of the class Examples:

#class asac:
 #   def __init__(self) -> None:
  #      self.name = NameError

#o = asac ('Yash')
#print(o.name)        
#print(o)
   
class Person:
    def __init__(self, firstname, lastname, age, country):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
p = Person('Yash', 'Tambe', 21, 'India')
  # Age should ideally be an integer
print(p.firstname, p.lastname, p.age, p.country)

#Obejct methods
#Objects can have methods. The methods are functions which belong to the object.
class Person:
    def __init__(self, firstname, lastname, age, country):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
    def person_info(self):
       return f'{self.firstname} {self.lastname} is {self.age} , He lives in {self.country}.'
 

#Object Dfault Methods
#Sometimes, you may want to have a default values for your object methods. If we give default values for the parameters in the constructor, we can avoid errors when we call or instantiate our class without parameters.
class Person:
    
    def __init__(self, firstname='Yash', lastname='Tambe', age='20', country='India'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
    def person_info(self):
       return f'{self.firstname} {self.lastname} is {self.age} , He lives in {self.country}.'
p1= Person()
print(p1.person_info())
p2 = Person('Shreyash','Tambe','18','Japan')
print(p2.person_info())

#Method to Modify Class Default Values
#he person class, all the constructor parameters have default values. In addition to that, we have skills parameter, which we can access using a method. Let us create add_skill method to add skills to the skills list.

class Person:
    
    def __init__(self, firstname='Yash', lastname='Tambe', age='20', country='India'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old, and lives in {self.country}.'

    def add_skill(self, skill):
        self.skills.append(skill)

p1 = Person()  # Uses default values
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
print(p1.skills)  # This will print the skills added to p1

p2 = Person('Shreyash', 'Tambe', 18, 'Japan')
print(p2.person_info())
p2.add_skill('React')
p2.add_skill('Data Analysis')
print(p2.skills)  # This will print the skills added to p2


#Inheritance
#Using inheritance we can reuse parent class code. Inheritance allows us to define a class that inherits all the methods and properties from parent class. The parent class or super or base class is the class which gives all the methods and properties. Child class is the class that inherits from another or parent class. Let us create a student class by inheriting from person class.

class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

#What You've Achieved:
#Inheritance: The Student class can now utilize all the functionalities of the Person class without needing to rewrite them.
#Reuse of Code: This makes your code more efficient and organized. You can add additional attributes or methods to Student later if students have unique characteristics or behaviors that don't apply to all persons.