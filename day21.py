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

class Person:
    def __init__(self) -> None:
        self.name =NameError

p = Person('Yash')
print(p.name)        
printt(p)