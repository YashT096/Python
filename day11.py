#Today , we are Learning about functions

#Syntax
 #def function_name():
   # codes
  #  codes

 #function_name()

def generate_full_name():
    first_name = 'Yash'
    last_name = "Tambe"
    space = " "
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () 

def add_two_numbers ():
    first_num = 4
    second_num = 8
    total_sum = first_num + second_num
    return(total_sum)
print(add_two_numbers ())    

#Function with parameters

#syntax
#def function_name(parameter):
   # codes 
   # codes

#print(function_name(argument))

def greetings (name):
    message = 'Hello '  + name + " ,Welcome to Python Everbody!!"
    return message

print(greetings('Yash'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

#Passing anargument with key and value 

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Yash', lastname = 'Tambe'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter