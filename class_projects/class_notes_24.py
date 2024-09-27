'''
script: class_notes_24sep.py
action: runs my class notes for the week
author: Dylan McCallum  
date: 24SEP24

'''

'''
2 types of files, Text, Binary

Consider storing 123

ASCII ---> 61, 62, 63 
       Text File ---> ([00111101], [00111110], [00111111])
        
Binary File ---> [01111011] = 123

Store in binary ==> less space

Some files require binary ==> Image / Audio files

All files have end of file marker EOF

Program writes to the file object

File Objects

When a program interface with a file it does it through a file object
    - Stores the Name of the file
    - Keeps track of current read location
    - File status 
    - Methods
        - read()
        - readline()
        - write()
        - close()
        
Files
    standard file objects
        sys.stdin ---> keyboard
        sys.stdout ---> monitor
        sys.stderr ---> file for error messages
    
    All can be redirected
    
Opening and Closing Files
    Opening
        - fileHandle ==> open(fileName: mode)
            mode can take 3 forms
                -r ==> read from the file
                -w ==> write to the file
                -a ==> appent to the file
        - Example
            patient = open('patientDataFile.txt', 'r')
    
    Closing
        - fileHandle ==> fileHandle.close()
        
        -Example
            patient.close()
        
        We should always close a file.

Processing
    Reading + Writing

        The read() method reads one line of text
            -> from the current marker position to end of file
            -> returns a single string
    Example

        patient1 = patient.read()
    
    Returns an empty string at the end of file
    
        The write() method writes to the file
            A string beginning at the current marker position
        
        Example 
            patient.write("Dylan, McCallum, Full HP)


'''

# Example of class

class Person:
    def _init__(self, f_name=str, l_name=str, social_num=str, salary=float):
        
        self.f_name = f_name
        self.l_name = l_name
        self.social_num = social_num
        self.salary = salary
    
 
myCounty = ['Pima', 'Cochise', 'Maricopa', 'Pinal', 'Yavapai', 'Yuma']

fh = open('outWords.txt', 'w')

for county in myCounty:
    fh.write(county + '\n')


fh.close()

