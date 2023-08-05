'''
Implement a program that reads a CSV file named "data.csv," containing columns
"Name" and "Age." Create a new CSV file called "adults.csv" with only the rows of
individuals who are 18 years or older
'''

import csv

def filter_adults(input_file, output_file):

    try:
        with open(input_file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # Filter rows for individuals who are 18 years or older
            adults_data = [row for row in csv_reader if int(row['Age']) >= 18]

        # Write the filtered data to a new CSV file
        with open(output_file, 'w', newline='') as output_csv:
            fieldnames = ['Name', 'Age']
            csv_writer = csv.DictWriter(output_csv, fieldnames=fieldnames)

            csv_writer.writeheader()
            csv_writer.writerows(adults_data)

        print(f"Filtered data of adults written to {output_file}.")
    except FileNotFoundError:
        print("Error: File not found!")

input_file = "data.csv"
output_file = "adults.csv"
filter_adults(input_file, output_file)
