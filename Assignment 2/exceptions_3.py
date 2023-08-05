"""
Math Operations Module

This module contains a function 'division' to perform division of two numbers.
"""

def division(num1, num2):
    """
    Return the quotient when num1 is divided by num2.

    Args:
        num1 (int): Dividend.
        num2 (int): Divisor.

    Returns:
        int: Quotient of num1 divided by num2.
    """
    try:
        quot = int(num1) / int(num2)
    except ZeroDivisionError:
        print("Zero Division Error: can't divide by 0")
        return None
    except ValueError:
        print("Value Error.")
        return None
    return quot

print("Try 1")
print("\n", division(10, 2))
print("\n\n")

print("Try 2")
print("\n", division('a', 3))
print("\n\n")

print("Try 3")
print("\n", division(5, 0))
