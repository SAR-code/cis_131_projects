#cis_131_mpg.py
'''
script: cis_131_mpg.py
action: A. Receives user input on miles driven and gallons used per fill 
        B. Calculates and displays the mpg obtained after each tankful
        C. Calculate and display combined mpg for all tankfuls
author: Dylan McCallum
date: 02SEP24

'''

# declare a main function to house all operations

def main():
    '''
    Runs the entire application by performing actions 'A', 'B', and 'C'
    as mentioned above. Declares local variables within the function

    action: Runs the script cis_131_mpg.py to invoke necessary functions 
            and run the while loops
            
    input: User inputs the miles driven and gallons consumed
    
    output: The miles driven per trip, gallons consumed per trip, and the mpg
            per trip. also outputs the combined miles, gallons, and mpg
    
    return: None
    
    '''

    # declare local variables and sentinel values

    miles_driven = 0
    gallons_used = 0
    miles_per_gallon = 0

    stop_input = 0    # sentinel value
    
    # outer-loop starts the script
    while stop_input == 0:
        
        # receives the user input on miles and gas
        
        get_miles_driven = float(input('How many miles have you driven? '))
        get_gallons_used = float(input('How many gallons have you used? '))
        
        miles_driven += get_miles_driven
        gallons_used += get_gallons_used
        miles_per_gallon = get_miles_driven / get_gallons_used
        
        print(f'miles: {miles_driven} \ngallons: {gallons_used}')
        print(f'The mpg for this tank was {miles_per_gallon}')
        
        # prompts user to continue to add input
        additional_inputs = str(input("Add another trip? Type 'y' or 'n' "))
        additional_inputs = additional_inputs.lower()
        
        if additional_inputs == 'y':
            continue
        elif additional_inputs == 'n':
            stop_input = -1
        else:
            print("Please enter either 'y' or 'n'.")
        
        # invokes get_combined_mpg to output the total numbers calculated
        
        get_combined_mpg(miles_driven, gallons_used)


# declare a function that calculate and displays total mpg and total tankfuls

def get_combined_mpg(total_miles: float, total_gallons: float ):
    '''
    Receives arguments for combined miles and gallons and outputs the
    total miles driven, total gallons used.
    
    action: Calculates total miles and total gallons consumed and outputs
            combined mpg
            
    input: Arguments for total miles and total gallons
    
    output: The calculated total mpg, miles driven, and gallons consumed
    
    return: None
    '''
    
    # calculates the combined total mpg
    
    combined_total_mpg = total_miles / total_gallons
    
    print(f'The total miles driven was {total_miles}',
          f'\nThe total gallons consumed was {total_gallons}',
          f'\nThe combined mpg for the trip is {combined_total_mpg}'
          )

# invokes main function
main()