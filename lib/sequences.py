#!/usr/bin/env python3
import ipdb

def print_fibonacci(length):
    fibonacci = []

    if length == 0:
        fibonacci
    elif length == 1:
        fibonacci = [0]
    elif length == 2:
        fibonacci = [0, 1]
    else:
        fibonacci = [0, 1]
        for i in range(2, length): 
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

    print(fibonacci)