'''
script: class_notes_15.py
action: runs my class notes for the week
author: Dylan McCallum  
date: 15OCT24
'''

# properties review

class Person(object):
    
    def __init__(self, name, id_num):
        self._name = name
        self._id_num = id_num
    
    def setName(self, in_name):
        self._name = in_name
    
    def getName(self):
        return self._name
    
    # comparison 
    
    @property
    def id_num(self):
        return self._id_num
    
    @id_num.setter
    def id_num(self, id_num):
        
        self._id_num = id_num
    
    def setId_num(self, in_id_num):
        self._id_num = in_id_num
    
    def getId_num(self):
        return self._id_num
    


person_one = Person('Joe', 1234)

person_one.setName("John")

print(f'Name is {person_one.getName()}')

'''
Abstract classes

- Inherit from the abstract base class

- Not intended to make instances

- Set requirements for descendant classes


'''