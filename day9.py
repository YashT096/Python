# Conditiinals 

if condition:
  #this part of code runs for truthy conditions
a = 3 
if a > 0:
  print('A is a positive number')
# If-Else

if condition:
  this part of code runs for truthy conditions 
else :
  this part of code runs for false conditions 


# if elif else
if condition:
    code
elif condition:
    code
else:
    code


#short Hand

code if condition else code

#Nested Conditions\

if condition:
    code
    if condition:
    code

#example 
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

#If condition and logical Operators 

if condition and condition:
    code

#example 
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

#If and or logical operators 
if condition or condition:
    code

#example
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')

