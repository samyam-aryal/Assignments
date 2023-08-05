import json

def add_to_json(filename, new_data):

    with open(filename, "r") as file:
        data = json.load(file)
    data.append(new_data)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

new_student = {"name": "Hanuman", "age": 35}
add_to_json("sample_json.json", new_student)
