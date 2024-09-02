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
    
    action:
    input: none
    output: none
    return: none
    
    '''
    print("Hello Main")
    
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
        
        print(f'miles: {miles_driven} \ngallons: {gallons_used}')
        
        # prompts user to continue to add input
        additional_inputs = str(input("Add another trip? Type 'y' or 'n' "))
        additional_inputs = additional_inputs.lower()
        
        if additional_inputs == 'y':
            continue
        elif additional_inputs == 'n':
            stop_input = -1
        else:
            print("Please enter either 'y' or 'n'.")


# declare a function to calculate and display mpg obtained each tankful


# declare a function that calculate and displays total mpg and total tankfuls

# invokes main function

main()