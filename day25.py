#Hello , Today we are going to look about Pandas
#Pandas is an open source, high-performance, easy-to-use data structures and data analysis tools for the Python programming language. 
# Pandas adds data structures and tools designed to work with table-like data which is Series and Data Frames. 
# Pandas provides tools for data manipulation.

import pandas as pd
import numpy as np

nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

#creating Pandas series with custom index
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

#creating pandas series from a dictionary
dct = {'name':'Yash','country':'India','city':'Vadodara'}
s = pd.Series(dct)
print(s)

#crating a pandas series using linspace
s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)


#Dataframes
#Pandas data frames can be created in different ways

data = [
    ['Yash', 'India', 'Vadodara'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

#Data Exploration
print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method

print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method


print(df.shape) # as you can see 10000 rows and three columns


print(df.columns)

heights = df['Height'] # this is now a series

heights = df['Height'] # this is now a series

print(heights)

weights = df['Weight'] # this is now a series

print(weights)

print(len(heights) == len(weights))

print(weights.describe())

print(df.describe())  # describe can also give statistical information from a dataFrame

