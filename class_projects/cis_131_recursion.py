'''
script: cis_131_recursion.py
action: Outputs the demonstration on recursion
author: Dylan McCallum
date: 25OCT24
'''

# declare a funtion to demo recursion

def recursion_example(base, exponent):
    '''
    Demonstrates how recursion operates using exponents
    
    action: Returns the exponent
    input: Base number and Exponent
    output: Print the base and exponent until the exponent is == to 1
    return: Returns the exponent based off input
    '''
    if (exponent == 1):
        return base
    else:
        print("Base:", base)
        print("Exponent:", exponent)
        return base * recursion_example(base, (exponent - 1))

# displays the recursion_example function

print(recursion_example(2,5))