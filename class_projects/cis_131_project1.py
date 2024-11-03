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
    # test_employee = Employee('Cloud', 'Strife', 777, 'soldier@mail', '520-123-4567', '001', '001', 3000, [2022, 2, 27]) 
    
    # print(test_employee.__repr__())
    # test_employee.f_name = 'Barret'
    # test_employee.l_name = 'Wallace'
    # test_employee.email_addr = 'avalanche@mail.com'
    # test_employee.role = '002'
    # test_employee.class_p = '001'
    # test_employee.phone_num = '619-221-8564'
    # test_employee.salary = 12000
    # print(f'\n{test_employee.__repr__()}')
    
    # create a list of employee objects
    employee_list = []
    
    # declare a function to get the employees
    
    def get_employees():
        
        # employee_files = open('employees.txt', 'r')
        
        # print(employee_files.read())
        
        with open('employees.txt', mode='r') as employees:
            
            organize_list = []
            
            for line in employees:
                organize_list.append(line.strip().split())
            
            del organize_list[0]
            
            for person in organize_list:
        
                        
                entered_employee = Employee(person[1], person[0], person[2],
                                            person[3], person[4], person[6],
                                            person[7], float(person[8]), [1,12,23]
                                            )
                
                print(entered_employee)
                print(person[5])
                
                
            
                
        
        
            
    
    # display two reports of employee data
    
        # Full Emploment Record
        
        # Contact Information
        
    # test functions, make sure you delete
    get_employees()
        

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
        
        self._email_addr =  email_addr
        
    
    @property
    def phone_num(self):
        '''returns the phone number'''
        # part_one = self._phone_num[0:3]
        # part_two = self._phone_num[3:6]
        # part_three = self._phone_num[6:]
        
        # self._phone_num = part_one + '-' + part_two + '-' + part_three
        
        return self._phone_num
    
    @phone_num.setter
    def phone_num(self, phone_num):
        
        if len(phone_num) != 12:
            raise Exception("Enter a proper phone number with dashes")
        
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
    
    # declare class variables
    role_dictionary = {'001':'Staff', '002': 'Faculty'}
    classification_dictionary = {'001': 'Full', '002': 'Part'}
    
    def __init__(self, f_name, l_name, id_num,
                 email_addr, phone_num, role,
                 class_p, salary, h_date 
                 ):
        
        '''Inherit from person and initialize each attribute'''
        
        super().__init__(f_name, l_name, id_num,
                       email_addr, phone_num
                       )
        
        # conditions for role_dictionary and assigning valid code
        self._role = self.get_keys_role(role)
        
        # conditions for classification_dictionary and assigning valid code
        self._class_p = self.get_keys_class(class_p)
        
        # indexing the list into different arguments
        self._h_date = date(h_date[0], h_date[1], h_date[2])
        
        # validating only positive numbers are entered
        
        if salary < 0:
            raise Exception("salary cannot be negative")
        else: 
            self._salary = float(salary)
    
    @staticmethod
    def get_keys_role(role):
        
        for key, value in Employee.role_dictionary.items():
            if value == role:
                return key
        
        return role
    
    @staticmethod
    def get_keys_class(class_p):
        
        for key, value in Employee.classification_dictionary.items():
            if value == class_p:
                return key

        return class_p
    
        
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
        
        if role in Employee.role_dictionary.values():
            self._role = role
        else:
            raise Exception("Incorrect role")
    
    
    @property
    def class_p(self):
        '''returns the person's classification'''
        return self._class_p
    
    @class_p.setter
    def class_p(self, class_p):
        '''Sets the person's classification'''
        
        if class_p not in Employee.classification_dictionary:
            raise Exception('Classification not found')
        else:
            self._class_p = Employee.classification_dictionary[class_p]
    
    
    @property
    def salary(self):
        '''Returns the salary'''
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        '''Sets the salary'''
        
        if salary < 0:
            raise Exception("New salary cannot be negative")
        else: 
            self._salary = float(salary)
        
    
    def __repr__(self):
        '''Return the repr for Employee'''
        
        return(f'***Employee*** {super().__repr__()}'
               f'\nRole: {self._role}'
               f'\nClassification: {self._class_p}'
               f'\nSalary: {self._salary:.2f}'
               f'\nHire Date: {self._h_date}'
               )

# invoke main function
main()