'''
script: cis_131_craps_game.py
action: The script simulates the dice game craps. The script keeps track
        of the win/lose percentages and calculates the updated percentage
        per roll.
author: Dylan McCallum
date: 19SEP24
'''

# imports the required modules
import random

# declare main function to house the other functions
def main():
    '''
    Runs the entire application to simulate the game of Craps. The script
    keeps tracks of whether the game was won or lost and the given percentage
    per each game. 
    
    action:
    input: None
    output:
    return: None
    
    '''
    
    # declare local variables and constants
    
    GAMES_PLAYED = 25
    
    game_count = 0
    game_roll_count = 0
    
    # declare local dictionaries to track game conditions
    
    my_wins = {
                1:0, 2:0, 3:0, 4:0, 5:0,
                6:0, 7:0, 8:0, 9:0, 10:0,
                11:0, 12:0, 13:0, 14:0, 15:0,
                16:0, 17:0, 18:0, 19:0, 20:0,
                21:0, 22:0, 23:0, 24:0, 25:0
               }
    
    my_loses = {
                1:0, 2:0, 3:0, 4:0, 5:0,
                6:0, 7:0, 8:0, 9:0, 10:0,
                11:0, 12:0, 13:0, 14:0, 15:0,
                16:0, 17:0, 18:0, 19:0, 20:0,
                21:0, 22:0, 23:0, 24:0, 25:0
               }
    
    my_results = {}
    
    test_dice = dice_roll()
    
    print(test_dice)

# declare function to roll the dice
def dice_roll():
    '''
    This function rolls two dice and returns the values as a tuple

    action: Uses the random function to get the results of the dice rolled
    input: None
    output: The results from the two dice after invoked by the random function
    return: Returns the results of the two dice rolls as a tuple
    
    '''
    print('Hello dice roll')
    
    dice_1 = random.randrange(1, 7)
    dice_2 = random.randrange(1, 7)
    
    return (dice_1, dice_2)

# declare function to display the dice roll
def display_dice_roll():
    print('Displaying dice')
# declare function to calculate sum of dice
def calculate_sum_of_dice():
    print('Calculating dice')
# determine sum based on first roll

# continue rolling until player wins or loses

# display win or lose message

# invokes main function to run the application
main()

'''
Notes to consider, erase when complete

dictionaries for my_wins and my_losses {1:0, 2:0, 25:0}
dictionaries for my_results 
GAMES_PLAYED = 10000
game_roll_count

GOST

Goals -> Qualitative
Objectives -> Quantitative
Strategies -> Qualitative
Tactics -> Quantitative

'''