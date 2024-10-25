'''
script: class_notes_22.py

'''

'''
Recursion

def factorial(n):
    if (n == 1):
        return n
    else:
        return (n * factorial(n-1))
        
General structure
    They either
        -solve part of the problem --> Base Case
        -reduces the size of the problem --> General Case
    
    we reduce the problem until we get to the base case
    
How to approach recursive problem

    three steps:
    
    Determine Base case
    
    Determine General case

Recursive functions use more memory than loops because the calling funtions are still in the stack when the successive recursive calls are made

Recursion is memory intensive

When to use recursion

    - the algorithm/data structure us suitable recursion
    - the code is shorter and more understandable
    - the solution runs within acceptable time and space limits

A recursive function is one that makes a call to itself in the body od the function
    
Motivation

Factorial
    5! = 5 * 4 * 3 * 2 * 1
        = 5 * 4!
        = 4 * 3!
        
    n! = n * (n - 1)!
    
    base n = 1
    
Fibonacci

1,1,2,3,5,8,13,21
f(1),f(2),f(3),f(4),f(5),f(6),f(7),f(8)

f(n) = f(n-1) + f(n-2) ----> General Case

Base Case f(1),f(2) = 1


'''

# Homework samples

# Base case n = 1
# General Case y = y * y^n-1

def power_function(y, n):
    
    # if statement
    
    if (n == 1):
        return y
    else:
        return y * power_function(y,(n-1))
    
    # else, call the function again

call_count = 0

def fibonacci(n):
    
    if( n == 0 or n == 1):
        
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# How many times do we call fibonacci
# Add external variable to count how many times we call fibonacci

def fib(n):
    if (n == 0 or n == 1):
        return (n, 1)
    else:
        (fib1, count1) = fib(n-1)
        (fib2, count2) = fib(n-2)
        
        fib_sum = fib1 + fib2
        countsum = count1 + count2 + 1
        return (fib_sum, countsum)

print(fib(4))

# return a tuple

'''
else:
    (fib1, count1) = fib(n-1)
    (fib2, count2) = fib(n-2)
    
    return (fib1 + fib2, count1 + count2 + 1)
'''