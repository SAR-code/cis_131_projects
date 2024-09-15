'''
script: cis_131_telephone.py
action: Receives user input in a form of a telephone number. The number input
        generates every possible seven letter word combination related to the
        number the user has given.
author: Dylan McCallum
date: 12SEP24

'''
# declare main function to hold the scripts operations

def main():
    print("Hello from main")
    
    # declare local variables to collect user input
    test_input = '2345678999'
    
    # invokes the get_telephone_words function
    get_telephone_words(test_input)




# declare function to generate word combination

def get_telephone_words(phone_num):
    '''
    This function receives the user's phone number as an argument and loops
    through the sequence of numbers. The output prints out every word 
    combination that can be created with the given number.
    
    action: returns every possible word combination from a given phone number
    
    input: the user's input becomes the argument for this function.
    
    output: outputs every word combination.
    
    return: none
    '''
    output = phone_num
    
    
    print(output)

# invokes main function

main()
