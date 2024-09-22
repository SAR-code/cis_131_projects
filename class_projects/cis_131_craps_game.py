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

    action: Runs the entire application to play a game of Craps and return the
            results.
            
    input: None
    
    output: The results of each game played with the percentage of win/lose 
            statistics associated with them.
            
    return: None

    '''

    # declare variable to receive the amount of games the user wants to play

    play_the_game = int(input("How many games would you like to play?: "))

    # invokes function to play the game and returns results from each roll

    get_craps_game_stats(play_the_game)


# declare function to roll the dice
def dice_roll():
    '''
    This function rolls two dice and returns the values as a tuple

    action: Uses the random function to get the results of the dice rolled
    input: None
    output: None
    return: Returns the random results of the two dice rolls as a tuple

    '''

    # declare dice variables

    dice_1 = random.randrange(1, 7)
    dice_2 = random.randrange(1, 7)

    # returns the random result of the dice

    return (dice_1, dice_2)

# declare function to calculate sum of dice
def calculate_sum_of_dice(dices :tuple):
    '''
    The function calculates the sum of both doce rolled by receiving the value
    of the dice as an argument

    action: Calculates the sum of the dice and returns the value
    input: The function receives the values of the dice as an arguent
    output: None
    return: The sume of two dice

    '''
    # returns the sum of the two dice

    return sum(dices) 

# declare a variable to run the game mechanics
def play_game():
    '''
    This function controls the logic on how the game is played by tracking
    the winning, losing, and point conditions.

    action: Track the winning/losing conditions of each roll
    input: None
    output: None
    return: The win/lose conditions based on first roll conditions or if
            the point matches, or losing condition of a 7 is met

    '''
    # declare variables to track the point and roll count

    my_point = 0
    roll_counter = 0

    # declare a while loop to cycle through iterations of the game

    while True:

        # increases roll count/invokes the dice roll and calculation functions

        roll_counter += 1
        current_roll = dice_roll()
        roll_result = calculate_sum_of_dice(current_roll)

        # conditional statements to determine won/lose status based on results

        if roll_counter == 1:
            # first roll results win or lose conditions

            if roll_result in (7,11):
                return 'You win!'
            elif roll_result in (2, 3, 12):
                return 'You lose!'
            else:
                my_point = roll_result
        else:
            # subsequent roll condtions if previous conditions were not met

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
    # declare local variables to track game play and report end results

    games_won = {}      # win dictionary
    games_lost = {}     # loss dictionary

    total_games_played = 0
    total_win_percentage = 0
    total_lost_percentage = 0

    # for loop to track win/lose conditions and stores them into dictionaries

    for num in range(num_of_games):
        result = play_game()
        total_games_played += 1

        # updates each of the dictionaries accordingly

        if result == 'You win!':
            if total_games_played not in games_won:
                games_won[total_games_played] = 0
            games_won[total_games_played] += 1
        elif result == 'You lose!':
            if total_games_played not in games_lost:
                games_lost[total_games_played] = 0
            games_lost[total_games_played] += 1

    # retrieves the sum of win/lose values from the dictionary

    games_won_sum = sum(games_won.values())
    games_lost_sum = sum(games_lost.values())

    # invokes function to display the total results

    get_game_conclusion(total_games_played, games_won_sum, games_lost_sum)
    
    # calculates the win/lose percentages  of each roll

    print("Rolls\tGames Won\tGames Lost\tWin %\t\tLose %\t\tTotal %")
    
    for game_roll in range(1, total_games_played + 1):
        winning_games = games_won.get(game_roll, 0)
        losing_games = games_lost.get(game_roll, 0)

        # The percentage calculation
        total_win_percentage += winning_games / games_won_sum * 100
        total_lost_percentage += losing_games / games_lost_sum * 100

        print(f"{game_roll}\t{winning_games}\t\t{losing_games}",
              f"\t\t{winning_games/total_games_played * 100:.2F}%",
              f"\t\t{losing_games/total_games_played * 100:.2F}%",
              f"\t\t{total_win_percentage:.2F}")


# declare function to display the conclusion of the game

def get_game_conclusion(game_total, total_games_won, total_games_lost):
    '''
    This function displays the percentage results from each game

    action: Displays the results based on the number of games played
    input: Receives the calculated totals from the game
    output: Displays the results
    return: None
    '''

    # variables to capture the arguments
    total_games_played = game_total
    games_won_sum = total_games_won
    games_lost_sum = total_games_lost

    # prints the display from the receive arguments

    print(f"\nTotal Games Played: {total_games_played}")

    print(f"Total Games Won: {games_won_sum}", 
          f"({games_won_sum / total_games_played * 100:.2F}%)")

    print(f"Total Games Lost: {games_lost_sum}", 
          f"({games_lost_sum / total_games_played * 100:.2F}%)\n")

# invokes main function to run the application
main()
