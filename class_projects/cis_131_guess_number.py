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
# import random module
import random

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
    # declare local variables and sentinel
    
    random_num = random.randint(1, 1000)
    num_of_guesses = 0
    play_again = 0      # sentinel value
    
    # local variables that contain string messages
    
    guess_msg = 'Guess my number between 1 and 1000 with the fewest guesses: '
    play_msg = "\nWould you like to play again? Enter 'y' or 'n': "
    
    # declare a while loop to track the amount of guesses
    
    while play_again == 0:
        
        # declare inner while loop to track the number of guesses
        
        while num_of_guesses < 10:
            
            # receives user's guess input
            users_guess_num = int(input(guess_msg))
            
            # conditional statements to determine the user's guess
            
            if users_guess_num > random_num:
                print("Too High. Try Again.")
                num_of_guesses += 1
            elif users_guess_num < random_num:
                print("Too Low. Try again")
                num_of_guesses += 1
            elif users_guess_num == random_num:
                
                # outputs congratulations message
                print("Congratulations! You guessed the number!")
                print(f"\nYou took {num_of_guesses} guesses\n")
                print("Either you know the secret or got lucky!")
                
                # users response to continue the game, resets local values
                user_response = str(input(play_msg)).lower()
                
                # conditional statement to compare user's response
                
                if user_response == 'y':
                    num_of_guesses = 0
                elif user_response == 'n':
                    play_again = -1
                else:
                    print("Please enter 'y' or 'no'")
            else:
                print("Enter only integers")
        
        # displays whether the user was successful or failed to guess
        
        if num_of_guesses < 11:
            print(f"\nYou took {num_of_guesses} guesses.\n")
            print(f"\nThe correct number was {random_num}")
            print("You should be able to do better")
        
        # users response on whether or not to continue playing the game.
        
        keep_going = str(input("Play again? Enter 'y' or 'n': ")).lower()
        
        # conditional statements to restart the while loops and guess count
        
        if keep_going == 'y':
            num_of_guesses = 0
            play_again = 0
        elif keep_going == 'n':
            play_again = -1
        
                
# invokes the main function
main()