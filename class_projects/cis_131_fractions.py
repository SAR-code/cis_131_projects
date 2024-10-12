'''
script: cis_131_fractions.py
action: runs the fractions module lab
author: Dylan McCallum  
date: 11OCT24
'''

# import fractions and module
from fractions import Fraction



# Declaring fractions in a variable

fraction_a = Fraction('2/4')
fraction_b = Fraction(13, 64)

# Adding two fractions

fraction_sum = fraction_a + fraction_b
print('The sum of the equation is:', fraction_sum)

# Subtracting two fractions

fraction_difference = fraction_a - fraction_b
print('The difference of the equation is:', fraction_difference)

# Multiplying fractions

fraction_product = fraction_a * fraction_b
print('The product of the equation is:', fraction_product)

# Dividing fractions

fraction_quotient = fraction_a / fraction_b
print('The quotient of the equation is:', fraction_quotient)

# Converting the quotient into a float

float_conversion = float(fraction_quotient)
print('The fraction quotient converted into a float:', float_conversion)

# Demostrating Python BUILT-IN TYPE COMPLEX
print("\n*****COMPLEX NUMBERS*****\n")

complex_num_a = complex(7, 3)       # first parameter is the real number, second is imaginary
complex_num_b = complex('28-11j')   # string type allows to determine whether its add or subtract

print(f'Printing complex numbers: {complex_num_a} and {complex_num_b}')

# Adding complex numbers

complex_sum = complex_num_a + complex_num_b
print('The sum of the complex equation is', complex_sum)

# Subtracting complex numbers

complex_difference = complex_num_a - complex_num_b
print('The difference of the complex equation is', complex_difference)

# Getting the real and imaginary parts of complex numbers

print(f" The {complex_num_a.real:.0f} is the real part of the complex number {complex_num_a}")
print(f" The {complex_num_a.imag:.0f}j is the imaginary part of the complex number {complex_num_a}")

