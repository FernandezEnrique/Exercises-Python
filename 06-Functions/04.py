#!/usr/bin/python3

# Define a function addition() and multip() that adds up 
# and multiplies all the number in a given list. 
# Ex. sum([1,2,3,4]) returns 10 and multip([1,2,3,4]) returns 24

def addition(numbers):
    value = 0
    for n in numbers:
        value += n
    return value

def multip(numbers):
    value = 1
    for n in numbers:
        value *= n
    return value

if __name__ == '__main__':
    numbers = [1,2,3,4]
    print(addition(numbers))
    print(multip(numbers))