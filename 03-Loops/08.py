#!/usr/bin/python3
#Enter a word to be spelled.

word = input("Enter a word: ")

for i in range(0, len(word)):
    if i != len(word)-1:
        print(word[i], end=",")
    else:
        print(word[i])