'''
script: cis_131_project1.py

action: Reads employee and student data from a file
        then stores data in objects and data stuctures
        then outputs data in a different display
        
author: Dylan McCallum
date: 31OCT24
'''

# import required modules

from abc import ABC
from datetime import date

# define a main function to run the entire script
def main():
    print("Hello from main")
    
    #test code
    
    
    # open a file that contains employee data
    
    # create a list of employee objects
    
    # display two reports of employee data
    
        # Full Emploment Record
        
        # Contact Information
        

# define abstract person class

class Person(ABC):
    '''Abstract class person'''
    
    def __init__(self, f_name =str, l_name =str, 
                 id_num =int, email_addr =str, phone_num =str):
        '''Initialize each attribute'''
        
        self._f_name =      f_name
        self._l_name =      l_name
        self._id_num =      id_num
        self._email_addr =  email_addr
        self._phone_num =   phone_num
    
    @property
    def f_name(self):
        '''returns the first name'''
        return self._f_name
    
    @property
    def l_name(self):
        '''returns the last name'''
        return self._l_name
    
    @property
    def id_num(self):
        '''returns the Id number'''
        return self._id_num
    
    @property
    def email_addr(self):
        '''returns the email address'''
        return self._email_addr
    
    @property
    def phone_num(self):
        '''returns the phone number'''
        return self._phone_num
    
    def __repr__(self):
        return (f'\nFirstName: {self.f_name}'
                f'\nLastName: {self.l_name}'
                f'\nId Number: {self.id_num}'
                f'\nEmail Address: {self.email_addr}'
                f'\nPhone Number: {self.phone_num}'
                )

class Employee(Person):
    '''Concrete Employee class inheriting from Person class'''
    
    def __init__(self, f_name =str, l_name =str, id_num =int,
                 email_addr =str, phone_num =str, role =str,
                 class_p =str, salary =float, h_date =object
                 ):
        
        '''Inherit from person and initialize each attribute'''
        
        super.__init__(f_name, l_name, id_num,
                       email_addr, phone_num, role,
                       class_p, salary, h_date)
        
        self._role = role
        self._class_p = class_p
        self._salary = salary
        self._h_date = h_date

# invoke main function
main()