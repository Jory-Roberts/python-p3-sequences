#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []
    first_value = 0
    second_value = 1
    temp_value = 0

    for i in range(length):
        if i in (0, 1):
            fibonacci_list.append(i)
        else:
            fibonacci_list.append(first_value + second_value)
            temp_value = second_value
            second_value = second_value + first_value
            first_value = temp_value

    print(fibonacci_list)















