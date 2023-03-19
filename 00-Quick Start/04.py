#!/usr/bin/python3

# Ask for hours worked and hourly rate and print how much charged

hours_worked = int(input("Hours worked: "))
hourly_rate = int(input("Hourly rate: "))

price = hours_worked * hourly_rate

print(f"Final price: ${price}")