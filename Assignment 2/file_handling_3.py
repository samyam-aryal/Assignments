"""
 file_handling_3.py
 This module is an exercise on file handling
"""


def search_log(log_file, search_keyword):
    """
    Search for a specific keyword in the given log file and print matching lines.

    This function reads the log_file line by line and checks if the search_keyword
    exists in each line. If found, it prints the line along with its line number.

    :param log_file: The path to the log file.
    :type log_file: str
    :param search_keyword: The keyword to search for in the log file.
    :type search_keyword: str
    """
    with open(log_file, 'r', encoding='UTF-8') as file:
        for line_number, line in enumerate(file, 1):
            if search_keyword in line:
                print(f"Line {line_number}: {line.strip()}")

if __name__ == "__main__":
    LOG_FILE = "example.log"
    SEARCH_TERM = "error"
    search_log(LOG_FILE, SEARCH_TERM)
