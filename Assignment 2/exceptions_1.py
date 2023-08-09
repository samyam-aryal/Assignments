'''
Write a Python program that takes two integers as input and performs division
(num1 / num2). Handle the ZeroDivisionError and display a custom error message
when the second number is zero.
'''

# I tried two approaches for this. The first method was explicitly
# assigning a condition and raising an Exception if that condition
# is met.
# # A try ... except code block outside the function handles the exception and
# generates exception message.


def division_first(num1, num2):
    """
    Return the quotient when num1 is divided by num2

    Args:
    num1 (int) : Divisor
    num2 (int) : Dividend  

    Returns:
    num1/ num2 (int) : Quotient of num1/num2
    """
    if num2 == 0:
        raise ZeroDivisionError("Can't divide by 0.")
    return num1/num2

try:
    print(division_first(10, 2), "First division method, try 1")
    print(division_first(5, 0), "First division method, try 2")
except ZeroDivisionError as z:
    print(z)

print("\n")
# The second approach is to use the base Exception class to automatically
# detect division by zero, and use the code block outside the function to 
# raise an appropriate exception message.


def division_second(num1, num2):
    """
    Return the quotient when num1 is divided by num2

    Args:
    num1 (int) : Dividend
    num2 (int) : Divisor

    Returns:
    num1 / num2 (int) : Quotient of num1/num2
    """
    try:
        return num1/ num2
    except ZeroDivisionError as exc:
        raise ZeroDivisionError("Can't divide by zero") from exc


try:
    print(division_second(10, 2), "Second division method, try 1")
    print(division_second(5, 0), "Second division method, try 2")
except ZeroDivisionError as z:
    print(z)

# try:
#     print(division_second(5, 0), "Second division method, try 2")
# except ZeroDivisionError as z:
#     print(z)
