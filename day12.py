#Today we are learining about modules.
#module is a file containing python definations and statements.
 

#day12.py

def generate_full_name(firstname, lastname):
    return firstname + " " + lastname

#Create another file with any name with.py extension
#mymodule.py file

import day12.py
print(day12.generate_full_name('Yash','Tambe'))
#It will print:- Yash Tambe

#Import Functions from a module

# mymodule.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Yash','Tambe'))
print(sum_two_nums(1,9))
mass = 100;
weight = mass * gravity
print(weight)
print(person['firstname'])


#importing functions  from a module and renaming 
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Yash','Tambe'))
print(total(1, 9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

#importing the In-built modules

# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()

#Math module

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

#random module
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
