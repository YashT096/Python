#Tuples

#Syntax
empty_tuple = ()
empty_tuple = tuple()

tpl = ( 'item1', 'item2','item3')

fruits = ('banana','Orange','Mango', 'Lemon')

print(len(tpl))
print(len(fruits))

#slicing the tuple

tpl = ( 'item1', 'item2','item3','item4')
all_items = tpl [0:4]
all_items = tpl[0:]
middle_items = tpl[1:3]

fruits = ('banana','Orange','Mango', 'Lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_Mango = fruits[1:3]  # doesn't include item at index 3
Orange_to_the_rest = fruits[1:]

#Range of Negative integers
fruits = ('banana','Orange','Mango', 'Lemon')
all_fruits = fruits[-4:]
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]

#Changing the tuples to list

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')


#Checking an item in tuple

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True


#Joining the tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

#Deleting the tuple


tpl1 = ('item1', 'item2', 'item3')
del tpl1
