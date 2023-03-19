#!/usr/bin/python3

# Define a function that checks if a string is a palindrome. 
# Example: "anna" is a palindrome but "car" is not

# To solve this one, we will use the reverse function
# We import it
from reverse_function import reverse

def is_palindrome(string):
    string_reversed = reverse(string)
    return (string == string_reversed)

if __name__ == '__main__':
    print(is_palindrome("anna")) # True
    print(is_palindrome("car"))  # False