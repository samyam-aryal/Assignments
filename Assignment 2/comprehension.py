# LIST COMPREHENSION
''' 
Q.  Given a list of strings, create a new list that contains only the
    strings with more than 5 characters using list comprehension.
'''
def length_filter(strings_list):
    return [s for s in strings_list if len(s) > 5]

print(length_filter(['ABC', 'abcdeg', 'samyam', 'sam', 'germany', 'goal']))

'''
Q.  Given two lists of integers, create a list that contains the
    product of each element of the first list with the corresponding element in the
    second list using list comprehension.
'''
def element_product(list1, list2):
    return [num1 * num2 for num1, num2 in zip(list1, list2)]

print(element_product([2,3,4], [2,3,4]))

##############################################################################################################################

# DICTIONARY COMPREHENSION

''' 
Q.  Given two lists - one containing keys and another
    containing values, create a dictionary using dictionary comprehension.
'''

def create_dict(list1, list2):
    return {key:value for key, value in zip(list1, list2)}

print(create_dict([1, 2, 3, 4], ['This', 'is', 'a', 'dictionary']))

'''
Q>  Create a dictionary using dictionary comprehension
    to represent the ASCII values of lowercase alphabets (a-z) where the keys are the
    alphabets, and the values are their corresponding ASCII values.
'''

import string
alphabet = string.ascii_lowercase

ascii_dict = {a:ord(a) for a in alphabet}
print("\n\n", ascii_dict)

##############################################################################################################################

# SET COMPREHENSION
'''
Q.  Given a list of numbers, create a set using set
    comprehension that contains only unique even numbers.
'''
def unique_even_num(input_numbers):
    return {num for num in input_numbers if num % 2 == 0}

print(unique_even_num([1,2,2,3,4,4,5,5,5,6,7,7,8,10,10]))


''' 
Q.  Given two strings, write a Python program to create a set
    using set comprehension that contains all the characters that are common in both
    strings.
'''

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

set1 = set(string1)
set2 = set(string2)
    
common = {char for char in set1 if char in set2}

print("Common characters in both strings:", common)

##############################################################################################################################