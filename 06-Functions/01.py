#!/usr/bin/python3

# Define a function max() that takes 2 numbers and returns max. 
# (Python already has a max() function though)

def max(a, b):
    larguest = 0
    if a > b:
        larguest = a
    else:
        larguest = b
    return larguest

if __name__ == '__main__':
    print(max(2,4)) # Prints 4