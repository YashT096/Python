#Dictionaries

empty_dict = {}

dict= {"key1" : "value1" , "key2" : "value2" , "key3" : "value3" }

person = {
    'first_name':'Yash',
    'last_name':'Tambe',
    'age':21,
    'country':'India',
    'is_marred':False,
    'skills':['JavaScript', 'HTML', 'CSS',  'Python'],
   
    }

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) 

# syntax - Adding items to a dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'

# Modifying item in a Dictionry

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'


#Getting Dictionary keys a list 

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])

#Getting Dictionary values as a list 

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
