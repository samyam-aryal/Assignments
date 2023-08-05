"""
exceptions_4.py

This module demonstrates the use of custom exceptions to handle invalid age values.
"""


class InvalidAgeError(Exception):
    """
    Custom exception for invalid age values.
    """

def get_age(age_str):
    """
    Convert the input age string to an integer and check if it's within the valid range.

    Args:
        age_str (str): The age as a string.

    Returns:
        int: The valid age as an integer.

    Raises:
        InvalidAgeError: If the age is not within the valid range (0 to 120).
    """
    age = int(age_str)
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")
    return age

if __name__ == "__main__":
    age_input = input("Enter age: ")

    try:
        valid_age = get_age(age_input)
        print("Age is:", valid_age)
    except InvalidAgeError as e:
        print(e)
