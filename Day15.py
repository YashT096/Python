#Today we'll Learn Python Error types

#When we write code it is common that we make a typo or some other common error. 
#If our code fails to run, the Python interpreter will display a message, containing feedback with information on where the problem occurs and the type of an error. 
#It will also sometimes gives us suggestions on a possible fix. Understanding different types of errors in programming languages will help us to debug our code quickly and also it makes us better at what we do.

#Syantax Error
# initialize the amount variable
amount = 10000

# check that You are eligible to
#  purchase Dsa Self Paced or not
if(amount>2999)
    print("You are eligible to purchase Dsa Self Paced")
#When the proper syntax of the language is not followed then a syntax error is thrown.

#Name Error

geek = input()
print(geek)
#NameError is raised when the identifier being accessed is not defined in the local or global scope. 

#index error

#The IndexError message in Python is a runtime error. 
#To understand what it is and how to fix it, you must first understand what an index is.
#A Python list (or array or dictionary) has an index. The index of an item is its position within a list. 
#To access an item in a list, you use its index.
test_list = [1, 2, 3, 4]
print(test_list[4])

# Module not found
yash@yash96:~$ python
Python 3.9.6 (default, Aug 26 2024, 14:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'

  #In the example above, I added an extra s to math deliberately and ModuleNotFoundError was raised. 
  #Lets fix it by removing the extra s from math.
>>>

  #Attribute Error

  yash@yash96:~$ python
Python 3.9.6 (default, Aug 26 2024, 14:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'>>>

#As you can see, I made a mistake again! Instead of pi, I tried to call a PI function from maths module.
#It raised an attribute error, it means, that the function does not exist in the module. Lets fix it by changing from PI to pi.


#key error
yash@yash96:~$ python
Python 3.9.6 (default, Aug 26 2024, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> users = {'name':'Yash', 'age':210, 'country':'India'}
>>> users['name']
'Yash'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>

#In the example above, a TypeError is raised because we cannot add a number to a string.


#Import Error
yash@Yash96:~$ python
Python 3.9.6 (default, Aug 26 2024 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>>
There is no function called power in the math module, it goes with a different name: pow.


#ValueError
yash@Yash96:~$ python
Python 3.9.6 (default, Aug 13,

Aug 26 2024, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
>>>
In this case we cannot change the given string to a number, because of the 'a' letter in it.

  

