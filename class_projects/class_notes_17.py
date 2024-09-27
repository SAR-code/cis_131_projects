'''
script: class_notes_17sep.py
action: runs my class notes for the week
author: Dylan McCallum  
date: 05SEP24

'''

# notes

# Dictionaries

'''
Dictionaries have key-value pairs. Consists of a list of key-value pairs

'''

my_book = { "Chapter 1": "The Beginning",
            "Chapter 2": "The Start",
            "Chapter 3": ["Two Chapters Here", "Another Chapter"],
            4.56: 'Float'
            }

#print(my_book)


print(my_book)

my_book["Chapter 3"] = my_book[1] = 'Changed Chapter'

print(my_book)

for item in my_book.keys():
    print(type(my_book[item]))
    
for value in my_book.values():
    print(value)
    
'''
Finite state machines

    fs1 -------------> fs2
    
'''

# Lisy Comprehensions
list1 = []
for item in range(1,6):
    list1.append(item)
    
list2 = list(range(1,6))

list3 = [item**3 for item in range(1,6)]

list4 = [item for item in range(1,11) if item%2 == 0]

print(list2, list3, list4)

colours = ['red','orange','yellow','green','blue']

colors = [item.upper() for item in colours]

print(colours, colors)

grades = {'Sue': [98, 87, 94], 'Bob': [84, 95, 91]}

grades2 = {k: sum(v) / len(v) for k, v in grades.items()}

print(grades2)