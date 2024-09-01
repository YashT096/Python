#Hello hello...
#Today we are going to know what is pip?
#PIP stands for Preferred installer program. 
# We use pip to install different Python packages. 
# Package is a Python module that can contain one or more modules or other packages.
#  A module or modules that we can install to our application is a package. 
# In programming, we do not have to write every utility program, instead we install packages and import them to our applications.

#download python then check whether you have pip intall or not
#if then you have to download pip through the cmd pip

>>> import numpy
>>> numpy.version.version
'1.20.1'
>>> lst = [1, 2, 3,4, 5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr)
5
>>> np_arr * 2
array([ 2,  4,  6,  8, 10])
>>> np_arr  + 2
array([3, 4, 5, 6, 7])
>>>

#import webbroswer module
import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)

#Uninstall packages
pip unistall packagename

#list of package 
pip list

#Show Package
pip show packagename

#the source is not enough to learn it through other souce and updatee this page later with more precise and better things.