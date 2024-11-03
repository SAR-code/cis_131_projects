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
    
    #test code
    test_employee = Employee('Cloud', 'Strife', 777, 'soldier@mail', '5201234567', '001', '002', 3000, [2022, 2, 27]) 
    
    print(test_employee.__repr__())
    
    test_employee.f_name = 'Barret'
    test_employee.role = '002'
    
    print(test_employee.role, '############')
    
    test_employee.phone_num = '6192218564'
    
    
    print(test_employee.__repr__())
    
    # open a file that contains employee data
    
    # create a list of employee objects
    
    # display two reports of employee data
    
        # Full Emploment Record
        
        # Contact Information
        

# define abstract person class

class Person(ABC):
    '''Abstract class person'''
    
    def __init__(self, f_name, l_name, 
                 id_num, email_addr, phone_num):
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
    
    @f_name.setter
    def f_name(self, f_name):
        '''sets the first name'''
        
        self._f_name = f_name


    @property
    def l_name(self):
        '''returns the last name'''
        return self._l_name
    
    @l_name.setter
    def l_name(self, l_name):
        '''sets the last name'''
        
        self._l_name = l_name
    
    
    @property
    def id_num(self):
        '''returns the Id number'''
        return self._id_num
    
    
    @property
    def email_addr(self):
        '''returns the email address'''
        return self._email_addr
    
    @email_addr.setter
    def email_addr(self, email_addr):
        '''sets email address'''
        
        self._email_addr = email_addr
        
    
    @property
    def phone_num(self):
        '''returns the phone number'''
        part_one = self._phone_num[0:3]
        part_two = self._phone_num[3:6]
        part_three = self._phone_num[6:]
        
        self._phone_num = part_one + '-' + part_two + '-' + part_three
        
        return self._phone_num
    
    @phone_num.setter
    def phone_num(self, phone_num):
        
        if len(phone_num) != 10:
            raise Exception("Enter a proper phone number")
        
        self._phone_num = phone_num
    
    def __repr__(self):
        return (f'\nFirstName: {self.f_name}'
                f'\nLastName: {self.l_name}'
                f'\nId Number: {self.id_num}'
                f'\nEmail Address: {self.email_addr}'
                f'\nPhone Number: {self.phone_num}'
                )

class Employee(Person):
    '''Concrete Employee class inheriting from Person class'''
    
    def __init__(self, f_name, l_name, id_num,
                 email_addr, phone_num, role,
                 class_p, salary, h_date 
                 ):
        
        '''Inherit from person and initialize each attribute'''
        
        super().__init__(f_name, l_name, id_num,
                       email_addr, phone_num
                       )
        
        # conditions for rol_dictionary and assigning the appropriate code
        
        role_dictionary = {'001':'Staff', '002': 'Faculty'}
        if role not in role_dictionary:
            raise Exception("role not found, enter 001 or 002")
        else:
            self._role = role_dictionary[role]
        
        self._class_p = class_p
        self._salary = salary
        
        self._h_date = date(h_date[0], h_date[1], h_date[2])
    
    @property
    def h_date(self):
        '''returns the hire date'''
        return self._h_date
    
    
    @property
    def role(self):
        '''returns the person's role'''
        return self._role
    
    @role.setter
    def role(self, role):
        '''Sets the person's role'''
        
        if role == "001":
            self._role = "Staff"
        elif role == "002":
            self._role = "Faculty"
        else:
            raise Exception("Enter 001 or 002")
    
    
    def __repr__(self):
        '''Return the repr for Employee'''
        
        return(f'***Employee*** {super().__repr__()}'
               f'\nRole: {self._role}'
               f'\nClassification: {self._class_p}'
               f'\nSalary: {self._salary}'
               f'\nHire Date: {self._h_date}'
               )

# invoke main function
main()