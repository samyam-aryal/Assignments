class InvalidAgeError(Exception):
    pass

def get_age(age):
    if int(age) < 0 or int(age) > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")
    return age


age = input("Enter age ")

try:
    age = get_age(age)
    print("Age is:", age)
except InvalidAgeError as e:
    print(e)
