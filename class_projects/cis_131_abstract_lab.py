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
        '''Initialize each attribute'''
        
        self._f_name = f_name
        self._l_name = l_name
        self._ssn = ssn
    
    @property
    def f_name(self):
        '''returns the first name'''
        return self._f_name
    
    @property
    def l_name(self):
        '''returns the last name'''
        return self._l_name
    
    @property
    def ssn(self):
        '''returns the SSN'''
        return self._ssn
    
    @abstractmethod
    def earnings(self):
        raise NotImplementedError('input code missing')
    
    def __repr__(self):
        return(f'\nFirstname: {self.f_name}' 
               f'\nLastname: {self.l_name} '
               f'\nSSN: {self.ssn}' )

# define concrete sub class of salaried employee

class SalariedEmployee(Employee):
    '''sub class salaried employee'''
    
    def __init__(self, f_name, l_name, ssn, w_salary):
        '''Initialize each attribute'''
        
        super().__init__(f_name, l_name, ssn)
        self._weekly_salary = w_salary
        
        # checks input for negative values
        if self._weekly_salary < 0:
            
            raise Exception('Salary cannot be negative')
    
    def __repr__(self):
        '''returns the repr for the salary employee'''
        
        return (f'\n****Salary Employee**** {super().__repr__()}'
                f'\nWeekly Salary: {self.weekly_salary}'
                f'\nEnd of Month Earnings:{self.earnings()}\n')
    
    @property
    def weekly_salary(self):
        '''returns weekly salary'''
        
        return self._weekly_salary
    
    @weekly_salary.setter
    def weekly_salary(self, salary_input):
        '''sets the weekly salary'''
        
        self._weekly_salary = salary_input
        
        if self._weekly_salary < 0:
            
            raise Exception("Salary cannot be negative")
    
    def earnings(self):
        '''calculates the weekly salary in the span on a month'''
        
        # calculates weekly salary for each month
        end_of_month_earnings = self.weekly_salary * 4
        
        # additional calculation to help set two different earnings methods
        return (f'\n\t- Salary for each week was ${self.weekly_salary}'
                f'\n\t- End of month total is ${end_of_month_earnings}')
        

# define concrete class for hourly employee 

class HourlyEmployee(Employee):
    '''sub class hourly employee'''
    
    def __init__(self, f_name, l_name, ssn, hours_worked, wage):
        '''Initialize each attribute'''
        
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
        
        return (f'\n****Hourly Employee**** {super().__repr__()}'
                f'\nHours Worked: {self.hours_worked} \nWages: {self.wages}'
                f'\nTotal Earnings: {self.earnings()}\n')
        
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
        '''calculates the hourly rate and wages'''
        
        # calculating the appropriate pay
        calculated_earnings = self.wages * self.hours_worked
        
        return (f'Your compensation is ${calculated_earnings:.2F}')

# Test Code

# employee_1 = HourlyEmployee('John', 'Wick', '11111', 168, 29.03)
# print(employee_1)

# employee_1.hours_worked = 72
# print(employee_1)

# employee_2 = SalariedEmployee('Koji', 'Shimazu', '41701', 1200.17 )
# print(employee_2)

# employee_2.weekly_salary = 5000.23
# print(employee_2)


