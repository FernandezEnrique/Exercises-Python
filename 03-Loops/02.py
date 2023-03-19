#!/usr/bin/python3
#Enter a positive integer and displays the countdown from that number to zero separated by commas.

number = int(input('Enter a positive whole number: '))

for i in range(number,-1,-1):
    print(i, end=", ")