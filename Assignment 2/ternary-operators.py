'''
Write a Python function called check_odd_even that takes an integer as input and
uses a ternary operator to return "Even" if the number is even, and "Odd" if the
number is odd.
'''

def check_odd_even(number):
    return "Even" if number % 2 == 0 else "Odd"


'''
Write a function find_bigger_number that takes three integers as input and uses a
ternary operator to return the larger number. If all numbers are equal, return
"Equal."
'''

def find_bigger_number(a, b, c):
    return "Equal." if a == b == c else (a if a >= b and a >= c else (b if b >= c else c))


'''
Create a Python function check_leap_year that takes a year as input and uses a
ternary operator to determine if it's a leap year. Return "Leap Year" if it is, otherwise
"Not a Leap Year." (A leap year is divisible by 4, except for years divisible by 100
but not divisible by 400).
'''

def check_leap_year(year):
    return "Leap Year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a Leap Year"

