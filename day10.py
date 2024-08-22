# Today we are going to learn Loops , types and examples...

#While loop 
  # exceutes the while loop untill the condition is fulfilling when the condtions gets flase its runs out of loop 
    #and Continue the rest block of code.

while condition:
   code gets run here

count = 0
while count < 5 :
  print(count)
  count = count + 1 

#Example 2
count = 0
while count < 5 :
  print(count)
  count = count + 1
else:
  print(count)

#Break and continue 

while condition:
  code gets run
  if another_Condition:
    break

#example
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

#Example 2
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

#For Loop

for iterator in 1st:
code gets runs

#Example:
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

#example 2
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

##


for iterator in sequence:
    code goes here
    if condition:
        break


numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

  # syntax
for iterator in sequence:
    code goes here
    if condition:
        continue


numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

#Nested Loop
# syntax
for x in y:
    for t in x:
        print(t)

#For else

# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

