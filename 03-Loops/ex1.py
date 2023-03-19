#!/usr/bin/python3
#Enter a positive integer and displays all odd numbers from 1 to that number separated by commas.

number = input('Enter a positive whole number: ')

if (number.isdigit()) and (int(number) >= 0):
    for i in range(0, int(number)):
        if i%2 != 0:
            print(i, end=", ")