#cis_131_guess_number.py
'''
script: cis_131_guess_number.py
action: Receives user input to guess a number between 1 to 1000. Based on the
        user input, the script returns a message stating whether the guess is
        too high or too low. The user will have to guess the correct number 
        within 10 guesses.
author: Dylan McCallum
date: 02SEP24
'''

# declare main function to house all of the operations

def main():
    '''
    Runs the entire application by receiving the user's input to determine
    whether the number they select is either correct, too high, or too low.
    The user has 10 chances to guess to guess correctly and should be prompted
    to play again.
    
    action: Runs cis_131_guess_number.py to invoke the necessary functions
            and run condtional statements based on the user input.

    input:  User will be prompted to enter a number to make a guess
    
    output: The output will display whether the guess was correct, too high,
            too low, or if the user runs out of guesses. The user will have 
            the option to play again.

    return: None
    '''
    print("hello main")

# declare a while loop to track the amount of guesses

# invokes the main function
main()