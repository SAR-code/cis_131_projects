'''
script: cis_131_grades.py
action: This script receives the user's input for grade entry and takes the 
        grades recorded and the class average and writes them to a text file.

author: Dylan McCallum
date: 28SEP24

'''

# declare a main function to hold program operations

def main():
    '''
    Runs the entire application by printing receiving the user's list of
    grades and writing the list of grades and the class average to a text file.
    
    action: Runs cis_131_grades.py script by retrieving the list of grades,
            calculating the class average, then writing the list of grades and
            class average result to a text file.
            
    input: None
    
    output: The script will output a text file with a list of grades and the
            the class average
            
    return: None
    
    '''
    
    # declare variables for while loop and function operations
    
    grade_list = []
    count = 0
    border = '*'
    
    # processess the grade the user inputs
    
    grade = int(input("Enter a grade. (Enter -1 to quit): "))
    
    # declare while loop to input grades
     
    while grade != -1:
        
        # exception handling to ensure the correct values are received
        try:
            # checks to make sure valid grades are entered
            
            if grade > 100 or grade < -1:
                print("Please enter a proper grade")
                grade = int(input("Enter a grade. (Enter -1 to quit): "))
                continue
                
            else:
                # adds the valid grades into the list and continues the count
                
                grade_list.append(grade)
                count += 1
                grade = int(input("Enter a grade. (Enter -1 to quit): "))
            
        except ValueError:
            # checks for improper values
            
            print("please enter a proper grade")    
        
        else:

           # stores the list of grades into a variable

           class_room_avg = get_class_total(grade_list)

           # outputs the variables into a formatted txt.file
           with open('grades.txt', mode='w') as grades:
                print(f'{"Grades":<10}', file = grades)
                print(f'{border * 16}\n', file = grades)
                
                # loops the individual grades into the file
                
                for item in grade_list:
                    print(item, file = grades)
                
               # outputs the class average
               
                print(f"\nThe class average is {class_room_avg:.2f}",
                          file = grades
                          )

    
    # reads the file previously written
    
    with open('grades.txt', mode='r') as grades:
        print(f'\n{"Grades":<10}')
        print(f'{border * 16}\n')
        
        class_avg_r = get_class_total(grade_list)
        
        for item in grade_list:
            print(item)
        
        print(f"\nThe class average is: {class_avg_r:.2f}")
        

# declare a function to calculate the class's grade average

def get_class_total(grades: list):
    '''
    This function receives the list of grades as an argument and returns the
    class grade average.
    
    action: Calculates the class average by receiving the list of grades and
            returning the average
            
    input: Receives a list of grades as an argument.
    
    output: None
    
    return: Returns the calculated class average
    '''
    
    class_sum = sum(grades)
    
    # gets the average of the grades submitted
    
    class_avg = class_sum /len(grades)
    
    return class_avg

# invokes main function

main()