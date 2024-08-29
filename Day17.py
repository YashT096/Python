#hello Hello 
#Today we are going to learn Exception handling

#Python uses try and except to handle errors gracefully.
#A graceful exit (or graceful handling) of errors is a simple programming idiom - a program detects a serious error condition and "exits gracefully", in a controlled manner as a result.
#  Often the program prints a descriptive error message to a terminal or log as part of the graceful exit, this makes our application more robust. 
# The cause of an exception is often external to the program itself.
#  An example of exceptions could be an incorrect input, wrong file name, unable to find a file, a malfunctioning IO device.
#  Graceful handling of errors prevents our applications from crashing.
#syntax
#try: 
       #code in this block if things go well
#except:   
        #code in this block run if things go wrong

try:
    print(10 + "5")
except:
    print("Something is wrong")

#example
try:   
    name = input('Enter your name:')   
    year_born = input('Year you were born:') 
    age = 2019 - year_born  
    print(f'You are {name}. And your age is {age}.')
except:  
    print('Something went wrong')        


#example:- different types of errors with except

try:   
    name = input('Enter your name:')   
    year_born = input('Year you were born:')    
    age = 2019 - year_born    
    print(f'You are {name}. And your age is {age}.')
except TypeError:  
    print('Type error occured')
except ValueError:    
    print('Value error occured')
except ZeroDivisionError:    
    print('zero division error occured') 

     