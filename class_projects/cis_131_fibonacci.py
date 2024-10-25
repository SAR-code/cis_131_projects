'''
script: cis_131_fibonacci.py
action: Outputs the demonstration on fibonaci
author: Dylan McCallum
date: 25OCT24
'''

# declare function to demonstrate fibonacci

def fibonacci(n):
    '''
    Demonstrates the fibonacci sequence
    
    action: returns the the amount of times fibonacci was called in a tuple
    input: a number represented by fibonacci
    output: None
    return: a tuple of the count_sum and how many times fiboncci was called
    
    '''
    
    if( n == 0 or n == 1):
        return (n, 1)
    else:
        (fib1, count1) = fibonacci(n - 1)
        (fib2, count2) = fibonacci(n - 2)
        
        fibonacci_sum = fib1 + fib2
        count_sum = count1 + count2 + 1
        
        # returns the tuple of the fib count and sum count
        return (fibonacci_sum, count_sum)
    
# display the invoked function's results

print(f'{fibonacci(10)} \n{fibonacci(20)} \n{fibonacci(30)}')