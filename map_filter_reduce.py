from functools import reduce
'''
MAP
Q.  Write a Python function square_numbers that takes a list of integers as
    input and uses the map function to return a new list containing the square of each
    element.
'''

def square_numbers(number_list):
    squared_list = list(map(lambda x : x**2, number_list))
    print(f"\nFor the list containing numbers {number_list}, \nthe list containing squared numebrs is {squared_list}")

square_numbers([1,3,4,7])


'''
FILTER
Q.  Write a Python function filter_long_strings that takes a list of strings as
    input and uses the filter function to return a new list containing strings with more
    than 5 characters.
'''

def filter_long_strings(list_of_strings):
    filter_for_strings = list(filter(lambda x: len(x)>5, list_of_strings))
    return filter_for_strings

list_of_random_words = ['Nepa', 'Nepalese', 'Fuse', 'Fusemachines', 'People', 'Men', 'Women', 'Indian']
filtered_list = filter_long_strings(list_of_random_words)
print("\nThe list containing strings with more than 5 characters is: ", filtered_list)

'''
REDUCE
Q.  Write a Python function calculate_factorial that takes an integer as input
    and uses the reduce function to return the factorial of that number.

'''

def calculate_factorial(number):
    factorial = reduce(lambda x, y:  x*y, range(1, number+1))
    print(f"\nThe factorial of {number} is {factorial}")

calculate_factorial(4)
