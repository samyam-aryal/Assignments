''' Write a Python program that takes a user input and converts it to an integer. Handle
the ValueError and display a custom error message when the input cannot be
converted to an integer.
'''

val = input("Enter the value to convert to integer data type: ")

try:
    new_val = int(val)
    print(new_val, " has been converted to type", type(new_val))
except ValueError:
    print("Value error: Unable to convert to integer")
