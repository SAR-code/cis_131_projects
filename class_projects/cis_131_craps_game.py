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

    # declare local variables and constants and empty dictionaries

    GAMES_PLAYED = 25

    game_count = 0
    game_roll_count = 0
    
    win_count = 0
    win_tracker = {}
    
    lose_count = 0
    lose_tracker = {}

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

    #dice_result = dice_roll()
    # dice_sum = calculate_sum_of_dice(dice_result)
    
    while game_count != GAMES_PLAYED:
        
        dice_result = dice_roll()
        game_roll_count += 1
        dice_display = calculate_sum_of_dice(dice_result)
        
        # dictates the game logic based on the first roll
        
        if dice_display in (7,11):
            win_count += 1
            game_count += 1
            if game_roll_count in my_wins:
                    my_wins[game_roll_count] += 1
            else:
                    my_wins[game_roll_count] =1
            game_result = 'Won'
        
        elif dice_display in (2, 3, 12):
            lose_count += 1
            game_count += 1
            if game_roll_count in my_loses:
                    my_loses[game_roll_count] += 1
            else:
                    my_loses[game_roll_count] =1
            game_result = 'Lost'
        
        else:
            game_result = 'Contine'
            my_point = dice_display
            print("My point is", dice_display)
            
        while game_result == 'Contine':
            dice_result = dice_roll()
            game_roll_count += 1
            
            new_dice_display = calculate_sum_of_dice(dice_result)
            
            if new_dice_display == my_point:
                game_result = 'Won'
                win_count += 1
                if game_roll_count in my_wins:
                    my_wins[game_roll_count] += 1
                else:
                    my_wins[game_roll_count] =1
                game_count += 1
                
            elif new_dice_display == 7:
                game_result = 'Lost'
                lose_count += 1
                if game_roll_count in my_loses:
                    my_loses[game_roll_count] += 1
                else:
                    my_loses[game_roll_count] =1
                game_count += 1
                
        print(f'wins: {win_count} \nlosses: {lose_count} \ngames played: {game_count}')
                
        
    
    


# declare function to roll the dice
def dice_roll():
    '''
    This function rolls two dice and returns the values as a tuple

    action: Uses the random function to get the results of the dice rolled
    input: None
    output: The results from the two dice after invoked by the random function
    return: Returns the results of the two dice rolls as a tuple

    '''
    
    # declare dice variables
    
    dice_1 = random.randrange(1, 7)
    dice_2 = random.randrange(1, 7)

    return (dice_1, dice_2)

# declare function to display the dice roll
def display_dice_roll(result :tuple):
    print(result)

# declare function to calculate sum of dice
def calculate_sum_of_dice(dices :tuple):
    '''
    The function calculates the sum of both doce rolled by receiving the value
    of the dice as an argument
    
    action: Calculates the sum of the dice and returns the value
    input: The function receives the values of the dice as an arguent
    output: The sum of the two dice
    return: None
    
    '''
    # Assigns two variables to the argument
    
    dice_one, dice_two = dices
    
    
    print(f'You rolled a {dice_one}, and a {dice_two}',
          f'for a total of {sum(dices)}')
    
    # displays the output of each dice and the calculated total
    
    return sum(dices) 


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