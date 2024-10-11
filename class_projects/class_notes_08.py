'''
script: class_notes_08.py
action: runs my class notes for the week
author: Dylan McCallum  
date: 08OCT24
'''

'''
class Person
    -name
    -dob

class Student can inhereit the properties of class Person    

class Employee
    -inherits Person class
    -hire date

##########################################################


class variable

my_class:
    - list [Bob, Alex]
    __init__()
    
    instance variables
    e.g
    name
    address
    phoneNumber
    ===========================> Instance of a class
                                my_class_one:
                                    Bob
                                    1234

    ============================> Instance of a class
                                    my_class_two:
                                        Alex
                                        5678
'''

class Person(object):
    
    #constructor
    def __init__(self, name, ID):
        
        self.name = name
        self.ID = ID
        
    def Display(self):
        print(self.name, self.ID)

class SalariedEmployee(Person):
    
    def __init__(self, name, ID, salary, post):
        self.salary = salary
        self.post = post
        
        Person.__init__(self, name, ID)
        
        # super().__init__(name, ID) # refers to the most base class
    
    def printUs(self):
        print("Employee class called")
    
    def Display(self):            # KNOWN AS FUNCTION OVERRIDE
        print(self.ID, self.name, self.salary, self.post)
        
    def getPay(self):
        return self.salary

class HourlyEmployee(Person):
    
    def __init__(self, name, ID, h_rate, h_worked, post):
        
        super().__init__(name, ID)
        self.h_rate = h_rate
        self.h_worked = h_worked
        self.post = post
    
    def getPay(self):
        pay = (self.h_rate * self.h_worked)
        return pay


myEmp = SalariedEmployee('Rome', 700, 500.00, 'intern')
myHourlyEmp = HourlyEmployee('Ron', 800, 20.00, 40, 'pipe fitter')

# print(myHourlyEmp.name, myHourlyEmp.getPay())
# print(myEmp.name, myEmp.getPay())

# staff = [myHourlyEmp, myEmp]

# for member in staff:
#     print(member.name, member.getPay())

# DAY TWO NOTES

class TestClass():
    # Class variable
    
    class_list = ['Charlie']
    
    def __init__(self, name):
        
        self.class_list = []
        self.class_list.append(name)
    

# pen = TestClass('Bob')
# print(pen.class_list)

# den = TestClass('Alice')
# print(den.class_list)

# print(TestClass.class_list)

# del pen.class_list
# print(pen.class_list)
# print(den.class_list)
# print(TestClass.class_list)


class Second_Person():
    
    contact_list = {}
    
    def __init__(self, name, p_number):
        self._name = name
        self._p_number = p_number
        
        self.contact_list[name] = p_number
    
    def displayDictionary(self):
        for k, v in self.contact_list.items():
            print(k, v)
    
person_one = Second_Person('Bob', 12345)
person_two = Second_Person('Alice', 67890)
person_three = Second_Person('Charlie', 24680)
person_four = Second_Person('Dave', 13579)

people = [person_one, person_two, person_three, person_four]

for friend in people:
    print('\n', friend._name)
    friend.displayDictionary()



