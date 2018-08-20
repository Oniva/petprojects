#! python 3
#  calcyears.py - calculate how many years are required for desired amount

tax = .94
interest = .08
comp_periods = 12
principal = 100
years = 5
amount = 100 * (1+interest/comp_periods) ** 60
print(amount)