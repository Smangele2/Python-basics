# Author: Smangele - Python basics

def greet(name):
    return f"Hello, {name}!"

def is_even(n):
    return n % 2 == 0

def filter_evens(numbers):
    new_list = []
    for n in numbers:
        if n % 2 == 0:
            new_list.append(n)
    return new_list

def sum_numbers(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def get_long_names(names):
    new_list = []
    for name in names:
        if len(name) > 5:
            new_list.append(name)
    return new_list
