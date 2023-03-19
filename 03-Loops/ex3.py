#!/usr/bin/python3
#Ask the user for an amount to invest, the annual interest and the number of years, then show the total amount obtained year by year.

amount = int(input("Amount to invest: "))
annualinterest = int(input("% Annual interest: "))
nyears = int(input("Number of years: "))

lastyear = 0
for i in range(0, nyears):
    lastyear = amount
    amount = amount * (1+annualinterest/100)
    print(f"You have {str(amount)}$.")
    print(f"So you have obtained {amount-lastyear}$ this year.")