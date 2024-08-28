#!/usr/bin/env python3

def print_fibonacci(length):


    # fibonacci_sequence = [0,1]

    # while len(fibonacci_sequence) < length:
    #     next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    #     fibonacci_sequence.append(next_value)

    #     print(fibonacci_sequence[:length])

    fibonacci_sequence =[]

    if length > 0:
        fibonacci_sequence.append(0)

    if length >= 2:
        fibonacci_sequence.append(1)

        for i in range(2, length):
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
    print(fibonacci_sequence)


print_fibonacci(10)