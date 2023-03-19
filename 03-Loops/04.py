#!/usr/bin/python3
#Ask the user for a positive integer and display a triangle based on * with the entered heigh.

number = int(input('Enter a positive whole number: '))

for i in range(1, number+1):
    for k in range(1, number+1-i):
        print(" ",end="")
    for j in range(0, i*2-1):
        print("*",end="")
    print("")
