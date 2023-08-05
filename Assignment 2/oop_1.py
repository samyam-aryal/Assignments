'''
Create a Python class to represent a University. The university should have
attributes like name, location, and a list of departments. Implement encapsulation to
protect the internal data of the University class. Create a Department class that
inherits from the University class. The Department class should have attributes like
department name, head of the department, and a list of courses offered. Implement
polymorphism by defining a common method for both the University and
Department classes to display their details.
'''

class University:
    def __init__(self, name, location):
        # Declaring variables as protected to protect its internal data
        self._name = name
        self._location = location
        self._departments = []
    
    def get_details(self):
        print(f"Details of the university are : \nName:{self._name}, \nLocation:{self._location}, \nList of Departments: {self._departments}")
        

class Department(University):
    def __init__(self, name, location, dept_name, dept_head, courses):
        super().__init__(name, location)
        self.dept_name = dept_name
        self.dept_head = dept_head
        self.courses = courses

    def get_details(self):
        print(f"Details of the department are: \nName:{self.dept_name}, \nDepartment Head:{self.dept_head}, \nCourses offered: {self.courses}")
        print("University Details are: ", self._name, self._location)
# tribhuwan = University("TU", "Kirtipur", ["Computer", "Physics"])
departments = Department("TU", "Kirtipur", "Computer", "Someone", ["CSIT", "CE"])

# tribhuwan.get_details()
departments.get_details()
