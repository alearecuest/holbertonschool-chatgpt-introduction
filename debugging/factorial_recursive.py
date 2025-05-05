#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Parameters:
        n (int): A non-negative integer for which the factorial is calculated.
        
    Returns:
        int: The factorial of n, which is the product of all positive
             integers less than or equal to n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
