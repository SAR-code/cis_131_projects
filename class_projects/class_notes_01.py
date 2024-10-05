'''
script: class_notes_01.py
action: runs my class notes for the week
author: Dylan McCallum  
date: 01OCT24
'''

'''
Dog ===> known as a class
    name
    breed
    birthDate
    
    bark()
    bite()
    eat()
    
    
puppy1 = Dog()      ====> puppy is an instance of the class Dog
puppy1.name = 'Spot'
puppy1.breed = 'Lab"

puppy1.bark()

puppy2 = Dog()


########################################

Properties
    -Can be stored in a class
    -Can be derived from values stored in a class
    -Appearance of attributes

Read/Write Property
    @property
    def property_name(self):
        return self.property_name
        
    @property_name.setter
    def property_name(self, value):
        *input validation to check correct inputs
        *data manipulation
        
        self._property_name = some_value_created
        
    @property
    def average(self):
        total = 0
        for keys in grades:
            total += grades
            average = total/grades
            return avg
            
Getters are read-only

Getters and setters signify that the function has read/write capabilities.



'''
# Account example
'''
self is needed. Without the parameter self, you will get an attribute error
'''
from decimal import Decimal

class Account:
    '''Account Class'''
    
    def __init__(self, name, balance, aPhone):      # method called when we instanciate an object
        '''Initialize an Account Object'''
        
        self.name = name
        self._balance = balance     # denotes a private variable in python
        self.phone = aPhone
        
    def deposit(self, amount):
        '''Deposit Money'''
        
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive')
        
        self._balance += amount
    
    def getBalance(self):       # Utilize the method to return the private variable _balance
        
        return self._balance

class Person:
    '''Person Class for future work'''
    
    def __init__(self, f_name, l_name, ID, email, phone):
        '''Initialize an object'''
        
        self.f_name = f_name
        self.l_name = l_name
        self.ID = ID
        self.email = email
        self.phone = phone

class Length:
    '''Experimenting with properties'''
    
    def __init__ (self, feet, inches):
        '''Convert internal representation'''
        self._total_inches = (feet * 12) + inches
    
    def __str__ (self):
        '''Return string of feet and inches'''
        return (str(self.feet) + 'ft ' + str(self.inches) + 'in')
        
    @property
    def inches(self):
        
        extra_inches = self._total_inches % 12
        
        return extra_inches
    
    @inches.setter
    def inches(self, incoming_inch):
        feet_inches = self._total_inches - self.inches
        
        self._total_inches = feet_inches + incoming_inch 
        

    
    @property
    def feet(self):
        the_feet = (self._total_inches - self.inches) /12
        return the_feet
    
        
        
def main():
    print ("Looking at Account \n")
    
    account1 = Account('John Green', Decimal('50.00'), "123-456-7890")
    
    account1.deposit(12)
    print("The account of", account1.name, "is:", account1.getBalance())    # getBalance method utilized to get the current balance
    
    account1.deposit(40)
    print("The account of", account1.name, "is:", account1.getBalance())
    
    person_1 = Person("Dylan", "McCallum", "86","d@mail.com", "123-456-7890")
    
    my_board = Length(100, 5)
    print(my_board)
    my_board.inches = 10
    print(my_board)

main()
        
    