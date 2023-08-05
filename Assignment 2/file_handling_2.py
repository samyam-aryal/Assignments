"""
 file_handling_2.py
 This module is an exercise on file handling
"""
import json

def add_to_json(filename, new_data):
    """
    Add new_data to the existing JSON data in the specified file.

    This function reads the JSON data from the given filename, appends the new_data to it,
    and then writes the updated JSON data back to the file.

    :param filename: The path to the JSON file.
    :type filename: str
    :param new_data: The data to be added to the JSON file.
    :type new_data: dict or list
    """
    with open(filename, "r", encoding='utf-8') as file:
        data = json.load(file)
    data.append(new_data)
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)

new_student = {"name": "Hanuman", "age": 35}
add_to_json("sample_json.json", new_student)
