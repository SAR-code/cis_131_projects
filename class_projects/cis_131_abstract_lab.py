'''
script: cis_131_abstract_lab.py
action: The script gets the payroll of the employees.
author: Dylan McCallum
date: 17OCT24
'''

# import required modules for the exercise

from abc import ABC, abstractmethod

# declare abstract base class Employee

class Employee(ABC):
    '''Abstract class Employee'''
    
    def __init__(self, f_name, l_name, ssn):
        self._f_name = f_name
        self._l_name = l_name
        self._ssn = ssn
    
    @property
    def f_name(self):
        return self._f_name
    
    @property
    def l_name(self):
        return self._l_name
    
    @property
    def ssn(self):
        return self._ssn
    
    @abstractmethod
    def earnings(self):
        raise NotImplementedError('input code missing')
    
    def __repr__(self):
        return(f'\nFirst Name: {self.f_name}' 
               f'\nLast Name: {self.l_name} '
               f'\nSSN: {self.ssn}')

# define concrete sub class of salaried employee

class SalariedEmployee(Employee):
    '''sub class salaried employee'''
    
    # def __init__(self, model, w_salary):
    #     super().__init__(model, w_salary)
    #     self._weekly_salary = w_salary
    
    def __init__(self, f_name, l_name, ssn, w_salary):
        super().__init__(f_name, l_name, ssn)
        self._weekly_salary = w_salary
    
    @property
    def weekly_salary(self):
        return self._weekly_salary

class HourlyEmployee(Employee):
    '''sub class hourly employee'''
    
    def __init__(self, f_name, l_name, ssn, hours_worked, wage):
        super().__init__(f_name, l_name, ssn)
        self._hours_worked = hours_worked
        self._wage = wage
        
        # validates hours for correct input
        if self._hours_worked < 0:
            
            raise Exception("Hours cannot be negative!")
        elif self._hours_worked > 168:
            
            raise Exception("Hours cannot exceed 168!")
        
        # validates wages to ensure no negative values are given
        if self._wage < 0:
            
            raise Exception("Wages cannot be negative!")
    
    def __repr__(self):
        '''returns the repr for the hourly employee'''
        
        return (f'Hourly Employee {super().__repr__()}'
                f'\nHours Worked: {self.hours_worked} \nWages: {self.wages}'
                f'\nTotal Earnings: {self.earnings()}')
        
    @property
    def hours_worked(self):
        '''returns the hours worked'''
        
        return self._hours_worked
    
    @hours_worked.setter
    def hours_worked(self, hour_input):
        '''Sets the hours worked'''
        
        self._hours_worked = hour_input
        
        # validates the hours submitted
        
        if self._hours_worked < 0:
            
            raise Exception("Hours cannot be negative")
        elif self._hours_worked > 168:
            
            raise Exception("Hours cannot exceed 168")

    @property
    def wages(self):
        '''Returns the wages given'''
        
        return self._wage
    
    @wages.setter
    def wages(self, wage_input):
        '''Sets the given wages for the employee'''
        self._wage = wage_input
        
        # validates wages to ensure negatives are not entered
        if self._wage < 0:
            raise Exception("Wages cannot be negative")
    
    
    def earnings(self):
        '''calculates the wage by taking the hours worked and multiplying by the wage'''
        
        # calculating the appropriate pay
        calculated_earnings = self.wages * self.hours_worked
        
        return (f'Your compensation is ${calculated_earnings:.2F}')
        
        

# Test Code

employee_1 = HourlyEmployee("John", "Wick", "11111", 168, 29.03)

print(employee_1)

employee_1.hours_worked = 72
print(employee_1.earnings())


