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
    '''
    Runs the entire application by receiving the user's input as a phone
    number without using 0's or 1's. The script will prompt the user to
    ensure the correct amount of digits have been entered
    '''
    
    # declare local variables to collect user input 

    user_message = ('Please enter a seven digit number without dashes, '
                    '1s, or 0s. ')
    good_input = False
    
    # while-loop to encase user makes the wrong input
    
    while good_input == False:
        
        # variable stores user input
        get_phone_number = str(input(user_message))
        
        # conditional statement to ensure the correct length
        if len(get_phone_number) != 7:
            
            #prompts the user to check the number of digits entered
            print('Enter seven digits')
            
        else:
            # invokes the get_telephone_words function
            get_telephone_words(get_phone_number)
            good_input = True


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
    # declare a list/matrix of numbers and letters
    
    my_letters = [
                    [],
                    [],
                    ['A','B','C'],
                    ['D','E','F'],
                    ['G','H','I'],
                    ['J','K','L'],
                    ['M','N','O'],
                    ['P','R','S'],
                    ['T','U','V'],
                    ['W','X','Y']
                    ]   
    
    # declare variable to hold the list of new words
    
    words_formed = []
    
    # declare variables and for-loops to iterate through the lists
    
    phone_num = int(phone_num)
    
    output = phone_num
    
    
    print(output)

# invokes main function

main()
