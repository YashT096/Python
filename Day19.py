#Hello Hello
#today we are going to learn file handling
#So far we have seen different Python data types.
#We usually store our data in different file formats. 
#In addition to handling files, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, .excel) in this section. 
#First, let us get familiar with handling files with common file format(.txt).
#File handling is an import part of programming which allows us to create, read, update and delete files. 
#In Python to handle data we use open() built-in function.

#syntax
open('filename',mode)
#mode( r,a,x,t,b) could be read , write and update.

#"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists
#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)

#openig files for reading
f = open(' ./files/reading_file_example.txt')
printf(f)
#As you can see in the example above, I printed the opened file and it gave some information about it. Opened file has different reading methods: read(), readline, readlines. An opened file has to be closed with close() method.
#read(): read the whole text as string. If we want to limit the number of characters we want to read, we can limit it by passing int value to the read(number) method.

f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()

#output
# output
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.

#opening the file for writing and updating
#Let udu append some text to the file we have been reading
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')

#the method below creats a new file. if the file does not exist 
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')

#deleting files
import.os
os.remove(,'./files/example.txt')

#or
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')

