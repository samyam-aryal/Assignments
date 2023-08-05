def search_log(log_file, search_keyword):

    with open(log_file, 'r') as file:
        for line_number, line in enumerate(file, 1):
            if search_keyword in line:
                print(f"Line {line_number}: {line.strip()}")


log_file_name = "example.log"
search_term = "error"
search_log(log_file_name, search_term)
