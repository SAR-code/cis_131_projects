# class_notes_05sep.py
'''
script: class_notes_05sep.py
action: runs my class notes for the day
author: Dylan McCallum  
date: 05SEP24

'''

# notes

'''
Lists- Ordered collection of mutable data.

a. Creating lists
    Enclosed in square brackets
    myList = []
    yourList = [1, 2, 4.8, 'Jim', (x,y)]

b. Adding elements to a list.
    myList.append('Pima')
    myList += ['School']
    newList = myList + yourList

c. Accessing Lists
    print(newList[1])

d. Editing Lists
    myList = newList[1] = 'County'

e. Remove elements from list
    myList.remove('item')
    
    del (myList[2])


ASCII NOTES



'''

myTuple = ('x', 4, 17.8)
print(myTuple)

myTuple = ( 95, [6,4,5], 8 )
print(myTuple[1][0])

myName = ['Dylan', 'J', 'McCallum']

for index, value in enumerate (myName):
    print(index, ':', value)
    
print( list(enumerate(myName)))