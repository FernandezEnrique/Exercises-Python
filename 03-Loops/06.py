#!/usr/bin/python3
# Ask for a number and show an odd based triangle like that:

# number = 5
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1 

number = int(input('Enter a positive whole number: '))

oddnumbers = []
last = 1
if (int(number) >= 0):
    for i in range(0, int(number)*2):
        if i%2 != 0:
            oddnumbers.insert(last, i)
            last = i

    for i in range(1, number+1):
        for j in range(i, 0,-1):
            print(str(oddnumbers[j-1]), end=" ")
        print("")
