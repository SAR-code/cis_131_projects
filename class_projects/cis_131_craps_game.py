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

    # GAMES_PLAYED = 25

    # game_count = 0
    # game_roll_count = 0
    
    # win_count = 0
    # win_tracker = {}
    
    # lose_count = 0
    # lose_tracker = {}

    # # declare local dictionaries to track game conditions

    # my_wins = {
    #             1:0, 2:0, 3:0, 4:0, 5:0,
    #             6:0, 7:0, 8:0, 9:0, 10:0,
    #             11:0, 12:0, 13:0, 14:0, 15:0,
    #             16:0, 17:0, 18:0, 19:0, 20:0,
    #             21:0, 22:0, 23:0, 24:0, 25:0
    #            }

    # my_loses = {
    #             1:0, 2:0, 3:0, 4:0, 5:0,
    #             6:0, 7:0, 8:0, 9:0, 10:0,
    #             11:0, 12:0, 13:0, 14:0, 15:0,
    #             16:0, 17:0, 18:0, 19:0, 20:0,
    #             21:0, 22:0, 23:0, 24:0, 25:0
    #            }

    # my_results = {}

    
    # while game_count != GAMES_PLAYED:
        
    #     dice_result = dice_roll()
    #     game_roll_count += 1
    #     dice_display = calculate_sum_of_dice(dice_result)
        
    #     # dictates the game logic based on the first roll
        
    #     if dice_display in (7,11):
    #         win_count += 1
    #         game_count += 1
    #         if game_count in my_wins:
    #                 my_wins[game_count] += 1
    #         my_wins[game_count] = 1
    #         game_result = 'Won'
        
    #     elif dice_display in (2, 3, 12):
    #         lose_count += 1
    #         game_count += 1
    #         if game_count in my_loses:
    #                 my_loses[game_count] += 1
    #         my_loses[game_count] = 1
    #         game_result = 'Lost'
        
    #     else:
    #         game_result = 'Continue'
    #         my_point = dice_display
    #         print("My point is", dice_display)
            
    #     while game_result == 'Continue':
    #         dice_result = dice_roll()
    #         game_roll_count += 1
            
    #         new_dice_display = calculate_sum_of_dice(dice_result)
            
    #         if new_dice_display == my_point:
    #             game_result = 'Won'
    #             win_count += 1
    #             if game_count in my_wins:
    #                 my_wins[game_count] += 1
    #             my_wins[game_count] = 1
    #             game_count += 1
                
    #         elif new_dice_display == 7:
    #             game_result = 'Lost'
    #             lose_count += 1
    #             if game_count in my_loses:
    #                 my_loses[game_count] += 1
    #             my_loses[game_count] = 1
    #             game_count += 1
                
    # print(my_wins)
    # print(my_loses)
    # print(f'wins: {win_count} \nlosses: {lose_count} \ngames played: {game_count}')
    
    # for key, value in my_wins.items():
    #     print(f'Wins: \n{key} : {value}')
        
    # for key, value in my_loses.items():
    #     print(f'Losses: \n{key} : {value}')
    
    play_the_game = int(input("How many games would you like to play?: "))
    get_craps_game_stats(play_the_game)


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
    # returns the sum of the two dice
    
    return sum(dices) 

# declare a variable to run the game mechanics

def play_game():
    '''
    This function controls the logic on how the game is played by tracking
    the winning, losing, and point conditions.
    
    action:
    input:
    output:
    return:
    
    '''
    my_point = 0
    roll_counter = 0
    
    while True:
        roll_counter += 1
        current_roll = dice_roll()
        roll_result = calculate_sum_of_dice(current_roll)
        
        if roll_counter == 1:
            if roll_result in (7,11):
                return 'You win!'
            elif roll_result in (2, 3, 12):
                return 'You lose!'
            else:
                my_point = roll_result
        else:
            if roll_result == my_point:
                return 'You win!'
            elif roll_result == 7:
                return 'You lose!'

# declare variable to get craps statistics

def get_craps_game_stats(num_of_games :int):
    '''
    This function gets the breakdown statistics of the number of games that
    were played and displays the win/loss ratios and percentages of all games 
    that were played.
    
    action:
    input:
    output:
    return:
    
    '''
    games_won = {}
    games_lost = {}
    
    total_games_played = 0
    total_win_percentage = 0
    total_lost_percentage = 0
    
    for num in range(num_of_games):
        result = play_game()
        total_games_played += 1
        
        if result == 'You win!':
            if total_games_played not in games_won:
                games_won[total_games_played] = 0
            games_won[total_games_played] += 1
        elif result == 'You lose!':
            if total_games_played not in games_lost:
                games_lost[total_games_played] = 0
            games_lost[total_games_played] += 1
    
    games_won_sum = sum(games_won.values())
    games_lost_sum = sum(games_lost.values())
    
    for game_roll in range(1, total_games_played + 1):
        winning_games = games_won.get(game_roll, 0)
        losing_games = games_lost.get(game_roll, 0)
        
        total_win_percentage += winning_games / games_won_sum * 100
        total_lost_percentage += losing_games / games_lost_sum * 100
        
        print(f"{game_roll}\t{winning_games}\t\t{losing_games}")
    
    get_game_conclusion(total_games_played, games_won_sum, games_lost_sum)

# declare function to display the conclusion of the game

def get_game_conclusion(game_total, total_games_won, total_games_lost):
    '''
    '''
    
    # variables to capture the arguments
    total_games_played = game_total
    games_won_sum = total_games_won
    games_lost_sum = total_games_lost
    
    print(f"\nTotal Games Played: {total_games_played}")
    
    print(f"Total Games Won: {games_won_sum}", 
          f"({games_won_sum / total_games_played * 100:.2F}%)")
    
    print(f"Total Games Lost: {games_lost_sum}", 
          f"({games_lost_sum / total_games_played * 100:.2F}%)")
    
# invokes main function to run the application
main()
