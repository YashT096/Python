# List comprehension 
# List comprehension in pythonis a compact way of creating a list from a sequence
#list comprehension is considerably faster then processing a list using instead of loop

#syntax

#[i for i in iterable if expression]

# if you want to change a string to a list of characters 


language = 'Python'
first = list(language) #changing the string to list 
print(type(first))  #list
print(first)

#2nd method 

first = [i for i in language]
print(type(first)) #list
print(first)

#for generating list of numbers

numbers = [ i for i in range(10)]
print(numbers)

squares = [ (i * i ) for i in range(10)]
print(squares)

#list of tuples
num = [ (i, i * i ) for i in range(10)]
print(num)

even_numbers = [i for i in range (21) if i % 2 == 0 ]
print(even_numbers)

odd_numbers = [ i for i in range(21) if i % 2 != 0 ]
print(odd_numbers)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ numbers for row in list_of_lists for numbers in row ]
print(list_of_lists)
print(flattened_list)

#Lamda function 
#Lambda function is a small anonymous function without a name. 
#It can take any number of arguments, but can only have one expression.
#Lambda function is similar to anonymous functions in JavaScript.

# syntax
x = lambda param1, param2, param3: param1 + param2 + param2
 # print(x(arg1, arg2, arg3))

 # Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22