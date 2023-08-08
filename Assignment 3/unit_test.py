'''
Q. Create a function that validates email addresses based on following set of rules:
- Proper email format such as presence of “@”, no space in the address
- Presence of valid email providers such as yahoo, gmail and outlook. Make sure
there are no no disposable email providers such as yopmail.
Write unit tests to validate different email addresses against the rules, including valid and
invalid addresses (Use unittest module).

'''

import re
import unittest

def validate_email(email):
    # Regular expression to check proper email format
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Regular expression to check valid email providers
    valid_providers = ['yahoo', 'gmail', 'outlook']
    invalid_providers = ['yopmail']
    
    # Check if email format is valid
    if not re.match(email_pattern, email):
        return False
    
    # Check if email provider is valid
    domain = email.split('@')[1]
    if domain in invalid_providers or domain.split('.')[0] not in valid_providers:
        return False
    
    return True

class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        valid_emails = [
            'user1@gmail.com',
            'samyam@yahoo.com',
        ]
        for email in valid_emails:
            self.assertTrue(validate_email(email))
    
    def test_invalid_emails(self):
        invalid_emails = [
            'user@gmail',
            'user@yopmail.com',
            'user @gmail.com',
            'user@outlook',
        ]
        for email in invalid_emails:
            self.assertFalse(validate_email(email))

if __name__ == '__main__':
    unittest.main()

################################################################################################

'''
Design a function that takes a list of numerical data and performs calculations for mean,
median and standard deviation. Write unit tests to verify the correctness of the statistical
calculations for various inputs, including edge cases like an empty list or a list with one
element (Use unittest module).
'''


import math
import unittest

def calculate_mean(data):
    """
    Calculate the mean (average) of the numerical data.

    :param data: List of numerical data.
    :type data: list of float or int
    :return: Mean value of the data.
    :rtype: float
    """
    if not data:
        raise ValueError("Cannot calculate mean of an empty list.")
    return sum(data) / len(data)

def calculate_median(data):
    """
    Calculate the median of the numerical data.

    :param data: List of numerical data.
    :type data: list of float or int
    :return: Median value of the data.
    :rtype: float
    """
    data.sort()
    n = len(data)
    mid = n // 2

    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]

def calculate_standard_deviation(data):
    """
    Calculate the standard deviation of the numerical data.

    :param data: List of numerical data.
    :type data: list of float or int
    :return: Standard deviation value of the data.
    :rtype: float
    """
    if len(data) < 2:
        raise ValueError("Standard deviation requires at least two data points.")
    
    mean = calculate_mean(data)
    squared_diff_sum = sum((x - mean) ** 2 for x in data)
    variance = squared_diff_sum / (len(data) - 1)
    return math.sqrt(variance)

class TestStatisticsCalculations(unittest.TestCase):
    def test_mean_calculation(self):
        self.assertAlmostEqual(calculate_mean([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(calculate_mean([10, 20, 30]), 20.0)
        self.assertAlmostEqual(calculate_mean([0]), 0.0)
        with self.assertRaises(ValueError):
            calculate_mean([])

    def test_median_calculation(self):
        self.assertAlmostEqual(calculate_median([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(calculate_median([10, 20, 30]), 20.0)
        self.assertAlmostEqual(calculate_median([1, 2, 3, 4]), 2.5)
        self.assertAlmostEqual(calculate_median([0]), 0.0)
        with self.assertRaises(ValueError):
            calculate_median([])

    def test_standard_deviation_calculation(self):
        self.assertAlmostEqual(calculate_standard_deviation([1, 2, 3, 4, 5]), 1.58113883, places=6)
        self.assertAlmostEqual(calculate_standard_deviation([10, 20, 30]), 10.0)
        self.assertAlmostEqual(calculate_standard_deviation([1, 2, 3, 4]), 1.29099445, places=6)
        with self.assertRaises(ValueError):
            calculate_standard_deviation([5])
        with self.assertRaises(ValueError):
            calculate_standard_deviation([])

if __name__ == '__main__':
    unittest.main()