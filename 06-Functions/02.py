#!/usr/bin/python3

# Define a function max_of_three() that takes 3 numbers
# and return the larguest one

def max_of_three(n1, n2, n3):
    numbers = [n1, n2, n3]
    larguest = numbers[0]
    for n in numbers:
        if n > larguest:
            larguest = n
    return larguest

if __name__ == '__main__':
    print(max_of_three(27, 22, 32)) # Prints 32