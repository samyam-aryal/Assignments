'''
ARGS
Q.  Write a Python function that takes an arbitrary number of positional
arguments and returns the sum of all the numbers. Test your function with various
input cases.


'''
def sum_of_numbers(*args):
    sum = 0
    for arg in args:
        sum+=arg
    return sum

print(sum_of_numbers(1,2,3,4))
print(sum_of_numbers(1,4,9,16,25,36,49))


'''
KWARGS
Q. Create a function create_student_report that takes the student's
    name as the first argument, the student's age as the second argument, and an
    arbitrary number of keyword arguments for the subjects and their respective
    scores. The function should return a dictionary with the student's information and a
    list of subjects along with their scores.
'''

def create_student_report(name, age, **kwargs):
    student_report = {"name":name, "age":age}
    for key, value in kwargs.items():
        student_report[key]=value
    return student_report


report_samyam = create_student_report("Samyam", 22, english=20, nepali=25)
print(report_samyam)

report_ram = create_student_report("Ram", 23, English=40, Nepali=20, Science=33)
print(report_ram)
