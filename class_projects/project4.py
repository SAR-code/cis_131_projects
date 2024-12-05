'''
script: project4Employess.py

action: Retrieves the average grade for each student, the class, and 
        displays the students that have made the honor roll

author: Dylan McCallum
date: 03DEC24
'''

# import required modules

from abc import ABC
from datetime import date



# define a main function to run the entire script
def main():
    '''Runs the entire script by reading the input file, processing its
        its contents, then displaying the file in one of two different outputs
        depending on what the user wants to see

        action: Reads information from the text file and creates sub-menus to 
                display specific formats of the file

        input: reads a given txt file

        output: returns two different displays after processing the txt file

        return: none
    '''

    # create a list of employee objects
    employee_list = []

    # create a list of student objects
    student_list = []

    # declare a function to get the employees

    def get_employees():
        '''
        This functions processess the contents in a txt.file and assigns each
        each field as an input to the Employee class. After each employee is 
        created, they get appended to a list containing employee objects

        action: reads the txt file and structures the information in order
                to be used in the Employee class

        input: none

        output: a newly formed list of employees based off the txt file

        return: none
        '''

        # using "with open" so the file closes on it's own

        with open('employees.txt', mode='r') as employees:

            # skips to the next line
            next(employees)

            # utilizing list as a placeholder
            organize_list = []

            # sectioning out each individual for a clean entry

            for line in employees:
                organize_list.append(line.strip().split())

            # display header
            print("Adding Employees\n")

            # loops through the list of clean employees
            for person in organize_list:

                # strips the slashes from the date for easier entry
                person[5] = str(person[5]).split('/')

                # validates the keys to ensure they are a match

                if ((person[6] == Employee.get_keys_role(person[6])) 
                    and person[7] == Employee.get_keys_class(person[7])
                    ):
                        # inputs the entries into the respective fields
                        entered_employee = Employee(person[1], person[0], 
                                                    person[2], person[3], 
                                                    person[4], person[6],
                                                    person[7], 
                                                    float(person[8]),
                                                     person[5])

                        # appends the newly formed list to the declared list
                        employee_list.append(entered_employee)

                        # displays each employee added
                        print(f"Added employee {entered_employee.f_name}"
                            f" {entered_employee.l_name}\n"
                            )


    # declare function to create menu

    def create_menu():
        '''
        This function creates a menu for the user to interact with the newly
        formatted txt files to display either employment information or 
        contact information

        action: displays the correct file output based on the user input by
                invoking the appropriate functions

        input: none
        output: different information displays
        return: none
        '''
        # declare a while loop to track menu items

        while True:

            # displays the menu options

            print("\nPlease select an option below")
            print("1. Quit")
            print("2. Display Employee Employment Information")
            print("3. Display Employee Contact Information")
            print("4. Display Student Contact Information")
            print("5. Display All Person Contact Information")
            print("6. Display Full Student Academic Scores")
            print("7. Display Academic Report for one Student")
            print("8. Display Honor Roll")

            try:
                selection = input("> ")

                # conditional statements based on the user input
                if selection == '1':
                    print("Thank you using the system.")
                    print("Now exiting the program...")
                    break

                elif selection == '2':

                    # displays employment information function
                    display_Employee_Employment_Information()
                elif selection == '3':

                     # displays employee contact information
                    display_Employee_Contact_Information()
                elif selection == '4':

                    # displays student contact information
                    display_student_contact_information()
                elif selection == '5':

                    # displays all contact information
                    get_all_person_info()
                elif selection == '6':

                    # displays student's scores
                    display_full_student_academic_report()
                elif selection == '7':
                    
                    # displays the full academic report on a single student
                    get_student_academic_report()
                elif selection == '8':
                    
                    # gets the students who are on the honor roll
                    get_honor_roll()
                else:

                    # if invalid entry has been made
                    print(f"I am sorry, {selection} is not an option.")
            except ValueError:
                print("Incorrect value entered")



    # display two functions/reports of employee data 

    # declare function for employment information

    def display_Employee_Employment_Information():
        '''
        The function organizes and displays the employee employment
        information

        action: takes the list of employees and outputs the information
                related to employment

        input: none

        output: displays each employee's employment information

        return: none

        '''

        # displays the title and header

        title = "Employee Employment Information\n"
        print(title.center(150))
        print(f'{"LastName" : <15} {"FirstName" : <15} {"ID" : <15}'
              f'{"Email" : <34} {"Phone" : <15} {"HireDate": <15}'
              f'{"Classification" : <25} {"Role" : <15}'
              f'{"Salary"}'
              )

        # iterates through the list of employees and displays the desired data

        for employee in employee_list:
            print(f"{employee.l_name : <15} {employee.f_name : <15}" 
                  f"{employee.id_num : <15} {employee.email_addr : <35}"
                  f"{employee.phone_num : <15} {str(employee.h_date) : <15}"
                  f"{employee.class_p : <25} {employee.role : <15}"
                  f"{employee.salary:.2f}"
                  )


    # Contact Information

    def display_Employee_Contact_Information():
        '''
        The function organizes and displays the employee contact
        information

        action: takes the list of employees and outputs the information
                related to contacts

        input: none

        output: displays each employee's contact information

        return: none

        '''

        # displays the title and header

        title = "Employee Contact Information\n"
        print(title.center(80))

        print(f'{"LastName" : <15} {"FirstName" : <15} {"ID" : <15}'
              f'{"Email" : <35} {"Phone"}'
              )

        # iterates through the list of employees and displays the desired data

        for employee in employee_list:
            print(f"{employee.l_name : <15} {employee.f_name : <15} " 
                  f"{employee.id_num : <14} {employee.email_addr : <35}"
                  f"{employee.phone_num}"
                  )


    # declare a function to get student info

    def get_students():
        '''
        This functions processess the contents in a txt.file and assigns each
        each field as an input to the Student class. After each student is 
        created, they get appended to a list containing student objects

        action: reads the txt file and structures the information in order
                to be used in the Student class

        input: none

        output: a newly formed list of students based off the txt file

        return: none
        '''

        # using 'with open' for auto closing

        with open('students.txt', mode = 'r') as students:

            # skips to the next line
            next(students)

            # placeholder list 
            organize_students = []

            # sectioning out each student for clean entry
            for line in students:
                organize_students.append(line.strip().split())

            # displays the title and header
        
            title = "Adding Students\n"
            print(title)

            # loops through a list of clean students

            for person in organize_students:

                # enters the respective student

                entered_student = Student(person[1], person[0],
                                          person[2], person[3],
                                          person[4]
                                          )

                # appends to student list

                student_list.append(entered_student)

                # displays each student added
                print(f"Added student {entered_student.f_name}"
                      f" {entered_student.l_name}\n"
                     ) 


    def get_student_scores():
        '''
        This function processess the contents in a txt.file
        and assigns each field as an input for scores in the Student class
        based on the student ID.

        action: reads the txt file and structures the scores ID to match the
                student's ID
                
        input: none

        output: a newly formed list combining part of the student information
                and connecting it to their respective subject scores

        return: none

        '''

        # using 'with open' for auto closing

        with open('scores.txt', mode = 'r') as students:

            # skips to the next line
            lines = students.readlines()[1:]

            # displays the title and header

            title = "Adding Student Scores\n"
            print(title)

            # Converts the txt file to int and maps through the list of scores

            for line in lines:
                data = line.split()
                student_id = int(data[0])
                scores = list(map(int, data[1:]))

                # Iterate through the student list and compares the ID numbers

                for student in student_list:
                    if student.id_num == student_id:
                        
                        # If ID's match, places the matching score
                        # and subject as a dictionary entry
                        
                        for index, score in enumerate(scores):
                            course = Student.course_name_list[index]
                            student.enter_scores(course, score)
                        
                        # outputs student scores that were added
                        
                        print(f"Added scores for {student.f_name} "
                              f"{student.l_name}...\n"
                              )


    def display_student_contact_information():
        '''
        The function organizes and displays the student contact
        information

        action: takes the list of students and outputs the information
                related to contacts

        input: none

        output: displays each student's contact information

        return: none

        '''

        # display title and header

        student_title = 'Student Contact Information\n'
        print(student_title.center(80))

        print(f'{"LastName" : <15} {"FirstName" : <15} {"ID" : <15}'
              f'{"Email" : <35} {"Phone"}'
              )

        # iterate through the list of students

        for student in student_list:
            print(f"{student.l_name : <15} {student.f_name : <15} " 
                  f"{student.id_num : <14} {student.email_addr : <35} "
                  f"{student.phone_num}"
                  )


    # declare a function to get all contact info

    def get_all_person_info():
        '''
        This function retrieves all contact information
    
        action: Function retrieves and displays all contact
                information

        input: None
        output: Displays all personnel contact info
        return: None

        '''

        # displays the title and header

        title = "All Person Contact Information\n"
        print(title.center(80))

        print(f'{"LastName" : <15} {"FirstName" : <15} {"ID" : <16}'
              f'{"Email" : <34} {"Phone"}'
              )

        # combines both lists

        master_contact_list = employee_list + student_list

        # iterates through the master contact list

        for person in master_contact_list:
            print(f"{person.l_name : <15} {person.f_name : <16}"
                  f"{person.id_num : <15} {person.email_addr : <35}"
                  f"{person.phone_num}"
                  )
    
    # declare a function to display an academic report for one student
    
    def display_full_student_academic_report():
        '''
        This function displays the full academic report with each student's 
        grade average as well as the class average
        
        action:
        input:
        output:
        return:
        
        '''
        
         # displays the title and header
        
        title = "Full Academic Report\n"
        print(title.center(180))

        print(f'{"LastName" : <15} {"FirstName" : <15} {"ID" : <15}', end="")

        # Displays the specific subject categories

        print(f'{Student.course_name_list[0] : <15} '
              f'{Student.course_name_list[1] : <15} '
              f'{Student.course_name_list[2] : <15} '
              f'{Student.course_name_list[3] : <15} '
              f'{Student.course_name_list[4] : <20} '
              f'{"High" : <15}'
              f'{"Low" : <15}'
              f'{"Average" : <15}'
              f'{"grade" : <15}'
              )

        # iterate through the list of student scores

        for student in student_list:
            grades = student.get_student_academics()
            
            # separates the grade portion of the list
            
            grade_list = slice(3,8)
            
            # creates a copy of the shortened list
            
            grade_numbers = list(grades[grade_list])
            
            # converts the grades into ints
            
            for num in range(len(grade_numbers)):
                grade_numbers[num] = int(grade_numbers[num])
            
            # retrieves the min and max from the list of grades
            
            grade_high = max(grade_numbers)
            grade_low = min(grade_numbers)
            
            # retrieves the average of each student
            
            grade_average = sum(grade_numbers) / len(grade_numbers)
            
            # declare variable for letter grade
            
            letter_grade = ''
            
            # assigns a letter grade based off the average score
            
            if grade_average >= 90:
                letter_grade = 'A'
                
            elif grade_average >= 80:
                letter_grade = 'B'
                
            elif grade_average >= 70:
                letter_grade = 'C'
                
            elif grade_average >= 60:
                letter_grade = 'D'
                
            else:
                letter_grade = 'F'
                
            # inserts student's firstname, lastname, and ID

            print(f"{grades[0] : <15} {grades[1] : <15} "
                  f"{grades[2] : <14}", end=""
                  )

            # inserts student's scores for respective subjects

            print(f" {grades[3] : <15} {grades[4] : <15}"
                  f" {grades[5] : <15} {grades[6] : <15}"
                  f" {grades[7] : <20} {grade_high : <14}"
                  f" {grade_low : <14} {grade_average : <15}"
                  f" {letter_grade : <15}"
                  )
            
        
    
    # declare a function to get the student academic report
    
    def get_student_academic_report():
        '''
        This function gets the academic report of a single student
        
        action:
        input: None
        output:
        return: None
        '''
        pass
    
    # declare a function to get the honor roll students
    
    def get_honor_roll():
        pass



    # Invoke required menu functions

    get_employees()
    get_students()
    get_student_scores()
    create_menu()


# define abstract person class

class Person(ABC):
    '''Abstract class person'''

    def __init__(self, f_name, l_name, 
                 id_num, email_addr, phone_num):
        '''Initialize each attribute'''

        self._f_name = f_name
        self._l_name = l_name

        id_num = str(id_num)

        # checks for 4 digits

        if len(id_num) != 4:
            raise Exception("Id needs to be 4 digits")
        else:
            self._id_num = int(id_num)


        self._email_addr = email_addr

        # checks for 12 digits

        if len(phone_num) != 12:
            raise Exception("Enter a proper phone number with dashes")
        else:
            self._phone_num = phone_num

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

        return self._phone_num

    @phone_num.setter
    def phone_num(self, phone_num):
        '''sets the phone number'''

        if len(phone_num) != 12:
            raise Exception("Enter a proper phone number with dashes")


        self._phone_num = phone_num

    def __repr__(self):
        '''Return person string for repr()'''

        return (f'\nFirstName: {self.f_name}'
                f'\nLastName: {self.l_name}'
                f'\nId Number: {self.id_num}'
                f'\nEmail Address: {self.email_addr}'
                f'\nPhone Number: {self.phone_num}'
                )

    def __str__(self):
        '''Prints the person class information'''

        return (f'\n***Person Info***'
                f'\nFirstName: {self.f_name}'
                f'\nLastName: {self.l_name}'
                f'\nId Number: {self.id_num}'
                f'\nEmail Address: {self.email_addr}'
                f'\nPhone Number: {self.phone_num}'
                )

# define concrete employee class 

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

        # checks and compares keys with the roles dictionary
        self._role = self.get_keys_role(role)

        # checks and compares keys with the classifications dictionary
        self._class_p = self.get_keys_class(class_p)

        # indexing the list into different arguments
        self._h_date = date(int(h_date[2]), int(h_date[0]), int(h_date[1]))

        # validating only positive numbers are entered

        if salary < 0:
            raise Exception("salary cannot be negative")
        else: 
            self._salary = float(salary)

    @staticmethod
    def get_keys_role(role):
        '''compares the role input with key/value pair in the dictionary'''
        for key, value in Employee.role_dictionary.items():
            if value == role:
                return key

        return role

    @staticmethod
    def get_keys_class(class_p):
        '''compares classification input with key/value pair in dictionary'''
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

        # checks the role entered
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

        # checks the classification entered
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
        '''Return the repr() for Employee'''

        return(f'{super().__repr__()}'
               f'\nRole: {self._role}'
               f'\nClassification: {self._class_p}'
               f'\nSalary: {self._salary:.2f}'
               f'\nHire Date: {self._h_date}'
               )

    def __str__(self):
        '''Returns the Employee class information'''

        return(f'\n***Employee Information***'
               f'{super().__str__()}'
               f'\nRole: {self.role}'
               f'\nClassification: {self.class_p}'
               f'\nSalary: {self.salary}'
               f'\nHire Date: {self.h_date}'
               )

# define concrete student class

class Student(Person):
    '''concrete student class inheriting from person class'''

    # declare class variables

    course_name_list = ['Art', 'Greek', 'Latin', 
                        'Science', 'Mathematics', 'Painting', 
                        'Sculpting'
                        ]

    def __init__(self, f_name, l_name, id_num, email_addr, phone_num):
        '''initialize each attribute'''
        super().__init__(f_name, l_name, id_num, email_addr, phone_num)
    
        # declare a dictionary to store scores for students
        self.courses_student_dict = {}


    def get_student_academics(self):
        '''Gets the student scores and compares them to the list'''

        # declare a list variable to store the scores
        grades = []

        for score in Student.course_name_list:
            grade = self.courses_student_dict.get(score, "Not Entered")
            grades.append(str(grade))

        updated_student_grades = [self._l_name, 
                                  self._f_name, 
                                  str(self._id_num)
                                  ] + grades

        return updated_student_grades


    def enter_scores(self, course, score):
        '''Enters the scores from the scores.txt file'''
        
        if course in Student.course_name_list and 0 < score < 101:
            self.courses_student_dict[course] = score
        else:
            raise Exception("Scores cannot be below 0 or above 100")


    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()
    
# invoke main function
main()