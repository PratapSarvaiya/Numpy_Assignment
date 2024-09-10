
'''
 r --> read mode
 w --> write mode
 a --> append mode
 r+ --> read and write
 w+ --> write and read
 a+ --> append and read
'''

# Open the file in the read mode
file = open("filehandling/file.txt","r")

# using file I can read

# Through loop
'''for line in file:
    print(line)
'''
#print(file.read())

# using with statement

'''with open("filehandling/file.txt",'r') as file:
    data = file.read()
    print(data)'''
    
# Read only the first x number of characters
'''with open("filehandling/file.txt",'r') as file:
    data = file.read(11)
    print(data)'''
    
# code for writing the file

'''file = open("filehandling/file2.txt",'w')
file.write("Hello world again")
file.write("First my students")
file.close()  '''

# code for the appending/writing to a file using with

'''with open("filehandling/file3.txt",'w') as file:
    file.write("Hello everyone") '''
    
import os

os.remove("filehandling/file3.txt")
    
    