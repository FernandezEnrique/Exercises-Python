#!/usr/bin/python3

# Ask for 2 numbers (m and n), it will print quotient and remainder

m = int(input("Enter dividend: "))
n = int(input("Enter dividor: "))

quotient = str(m // n)
remainder = str(m % n)

print(f"Quotient: {quotient}. Remainder: {remainder}")