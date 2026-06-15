"""
This is the DAY 7 of learning PYTHON.
"""

                                    #FILE I/O in PYTHON
"""
Python can be used to perform operations on a file, like read, write, etc.                                    

There are to types of files:

Text files: .txt, .docx, .log, etc.  #character files
Binary files: .mp4, .mov, .png, .jpeg, etc. #All non character files
"""

                                   # OPEN, READ & CLOSE FILE

"""
WE NEED TO OPEN FILE BEFORE READING OR WRITING.


SYNTAX: f= open("file_name", "mode") # mode= read ("r") or write ("w")
then we need to perform operations:

data= f.read() #to read file
data= f.close() #to close file
"""

#To open and read file & then close file:

i = open("day2.py", "r")
data= i.read()

print(data)
data= i.close()
print(data)

#To read some letters in file:
f= open("day3.py", "r")
data= f.read(500)
print(data)

#To print first lines of file:
"""
SYNTAX: data= f.readline()
"""
file= open("demo.file", "r")
x = file.readline()

print(x)

                                            #WRITE & APPEND IN FILE
#to overwrite file
f= open("demo.file", "w")
f.write("I WANT TO LEARN JAVASCRIPT")

#to append and write in the end of file:
f=open("demo.file", "a")
f.write( "\n THEN I AM GOING TO HTML")

                                            # all modes in file handling:
"""
r: read (default)
w: write (overwrite)
a: append (write in the end of file)
x: create (create file if not exist)
b: binary (for non character files)
t: text (default)
+: read and write
"""        
 
                                          #with syntax:
"""
with open("demo.file", "r") as f:
    data= f.read()
    print(data)
"""                                

                                        # Deleting file:
""" 
SYNTAX:
import os
os.remove("file_name")
"""

"""
DAY 7 IS COMPLETED.
"""
