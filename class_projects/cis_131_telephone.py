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
    
    action: Runs the cis_131_telephone.py script to invoke the necessary 
            functions and compute the users phone number input into a list 
            of all combination of words.
    
    input: User will be prompt to enter a phone number
    
    output: The output will display the various combination of words
            created from the seven digit number.
            
    return: None
    '''
    
    # declare local variables to collect user input 

    user_message = ('Please enter a seven digit number without dashes, '
                    '1s, or 0s. ')
    good_input = False
    
    # while-loop in case user makes the wrong input
    
    while good_input == False:
        
        # variable stores and checks user input
        get_phone_number = str(input(user_message))
        
        # conditional statement to ensure the correct length
        if len(get_phone_number) != 7:
            
            #prompts the user to check the number of digits entered
            print('Enter seven digits')
            
        else:
            # invokes the get_telephone_words function
            word_list = get_telephone_words(get_phone_number)
            
            # the mapped list writes to a file and prints words individually
            
            telephone_file = open('telephone.txt', 'w')
            
            # takes the mapped list and writes each word into a text file
            for item in word_list:
                print(item)
                telephone_file.write(item + '\n')
            
            # closes the txt file once the iteration is complete
            telephone_file.close()
            
            
            # displays the total number of combinations for the number entered
            
            print(f"\nA total of {len(word_list)} words in this combination")
            good_input = True
    
    


# declare function to generate word combination

def get_telephone_words(phone_num: str):
    '''
    This function receives the user's phone number as an argument and loops
    through the sequence of numbers. The output prints out every word 
    combination that can be created with the given number.
    
    action: Returns every possible word combination from a given phone number
    
    input: The user's input becomes the argument for this function.
    
    output: Outputs every word combination.
    
    return: Returns the mapped list of the possible word combinations
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
    
    # invoke function to retrieve the combination of words formed
    
    combinations_formed(phone_num, my_letters, 0,"", words_formed)
    
    # returns the possible combination of words
    
    return words_formed

# declare function to gather the list of all possible word combinations

def combinations_formed(num_list, map, index, current, words_formed):
    '''
    This function receives the arguments for the number list, mapping,
    the index, current number/letter and words formed then calls itself
    again for the next iteration.
    
    action: Takes in the arguements to create a word and then add it appending
            it to a list. This list contains all of the possible combinations 
            that can be created.
            
    input: The num_list which is the phone number that was input, a mapping
            function, the index position, current number/letter, and the 
            resulting formed word.
            
    output: Generates the list of all possible word combinations based off the 
            phone number that was received.
            
    return: None
    
    '''
    # maps the digits and letters based on input
    
    if index == len(num_list):
        words_formed.append(current)
        return
    
    # retrieves the letters mapped to the digits
    letters = map[int(num_list[index])]
    
    # Adds all of the letters to the formed word and calls on itself again
    # for the next iteration.
    
    for l in letters:
        combinations_formed(num_list, map, index + 1, current + l, words_formed)


# invokes main function

main()

