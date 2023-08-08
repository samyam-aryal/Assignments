import json

STUDENT_RECORDS_FILE = "student_records.json"

def load_records():
    """
    Load the student records from the JSON file.

    Returns:
        dict: Dictionary containing the student records.
    """
    try:
        with open(STUDENT_RECORDS_FILE, "r") as file:
            records = json.load(file)
    except FileNotFoundError:
        records = {}
    return records

def save_records(records):
    """
    Save the student records to the JSON file.

    Args:
        records (dict): Dictionary containing the student records.
    """
    with open(STUDENT_RECORDS_FILE, "w") as file:
        json.dump(records, file, indent=4)

def add_student(student_id, name, age, grade):
    """
    Add a new student to the records.

    Args:
        student_id (int): The ID of the student.
        name (str): The name of the student.
        age (int): The age of the student.
        grade (str): The grade of the student.
    """
    records = load_records()
    records[student_id] = {"name": name, "age": age, "grade": grade}
    save_records(records)

def search_student(query):
    """
    Search for a student by student_id or name.

    Args:
        query (int or str): The student_id or name of the student to search for.

    Returns:
        dict or None: Dictionary containing age and grade of the student if found, None otherwise.
    """
    records = load_records()
    for student_id, student_data in records.items():
        if query == student_id or query.lower() in student_data["name"].lower():
            return {"age": student_data["age"], "grade": student_data["grade"]}
    return None

def update_student(query, field, new_value):
    """
    Update a student's information by using student_id or name.

    Args:
        query (int or str): The student_id or name of the student to update.
        field (str): The field (age or grade) to update.
        new_value (int or str): The new value for the specified field.
    """
    records = load_records()
    for student_id, student_data in records.items():
        if query == student_id or query.lower() in student_data["name"].lower():
            if field == "age":
                student_data["age"] = new_value
            elif field == "grade":
                student_data["grade"] = new_value
            save_records(records)
            return

while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student Information")
    print("4. Exit")
    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        grade = input("Enter Student Grade: ")
        add_student(student_id, name, age, grade)
        print("Student added successfully!")

    elif choice == 2:
        query = input("Enter Student ID or Name to search: ")
        result = search_student(query)
        if result:
            print(f"Age: {result['age']}, Grade: {result['grade']}")
        else:
            print("Student not found!")

    elif choice == 3:
        query = input("Enter Student ID or Name to update: ")
        field = input("Enter field (age or grade) to update: ")
        new_value = input("Enter new value: ")
        update_student(query, field, new_value)
        print("Student information updated successfully!")

    elif choice == 4:
        break

    else:
        print("Invalid choice. Please try again.")
