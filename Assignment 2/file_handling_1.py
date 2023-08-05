"""
 file_handling_1.py
 This module is an exercise on file handling
"""

import csv

def filter_adults(input_file, output_file):
    """
    Reads a CSV file containing columns "Name" and "Age" and creates a new CSV file
    called "adults.csv" with only the rows of individuals who are 18 years or older.

    :param input_file: Path to the input CSV file.
    :param output_file: Path to the output CSV file.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # Filter rows for individuals who are 18 years or older
            adults_data = [row for row in csv_reader if int(row['Age']) >= 18]

        # Write the filtered data to a new CSV file
        with open(output_file, 'w', newline='', encoding='utf-8') as output_csv:
            fieldnames = ['Name', 'Age']
            csv_writer = csv.DictWriter(output_csv, fieldnames=fieldnames)

            csv_writer.writeheader()
            csv_writer.writerows(adults_data)

        print(f"Filtered data of adults written to {output_file}.")
    except FileNotFoundError:
        print("Error: File not found!")

INPUT_FILE = "data.csv"
OUTPUT_FILE = "adults.csv"
filter_adults(INPUT_FILE, OUTPUT_FILE)
