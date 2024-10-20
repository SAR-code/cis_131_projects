'''
script: cis_131_abstract_lab_test.py
action: This script tests the employee classes
author: Dylan McCallum
date: 17OCT24
'''
# import classes from cis_131_abstract_lab

from cis_131_abstract_lab import Employee, SalariedEmployee, HourlyEmployee

# declare Employee object for TypeError

'''
The following code will result in a TypeError
'''

# regular_employee = Employee('John', 'Smith', '123')
# print(regular_employee) 

# declare hourly and salaried employee objects

junior_employee = HourlyEmployee('Peter', 'Parker', '456', 120, 17.87)
senior_employee = SalariedEmployee('Tony', 'Stark', '789', 57345.89)

# display each employee representation and earnings

print(junior_employee)
print(senior_employee)

# iterate through the list of employees

morning_shift = [junior_employee, senior_employee]

# displays the string representation from the Employee class and earnings

for member in morning_shift:
    print('Firstname:', member.f_name)
    print('Lastname:', member.l_name)
    print('SSN:', member.ssn)
    print("Earnings:", member.earnings() + '\n')


