#!/usr/bin/env python3

def print_fibonacci(length):
    """Prints a list containing the Fibonacci sequence up to the specified length"""
    fibonacci_list = []
    
    # Handle length 0 (empty list)
    if length == 0:
        print(fibonacci_list)
        return
    
    # Handle length 1 (just 0)
    if length == 1:
        fibonacci_list.append(0)
        print(fibonacci_list)
        return
    
    # Handle length 2 (0, 1)
    if length == 2:
        fibonacci_list.extend([0, 1])
        print(fibonacci_list)
        return
    
    # Handle length 3 or more
    # Start with first two numbers
    fibonacci_list = [0, 1]
    
    # Generate remaining numbers
    for i in range(2, length):
        next_number = fibonacci_list[i-1] + fibonacci_list[i-2]
        fibonacci_list.append(next_number)
    
    print(fibonacci_list)