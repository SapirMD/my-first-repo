from Student import Student
from Employee import Employee
from Person import Person

student = Student("Alex", 30, "English", 3 ,85)
# student.foo()

employee = Employee("John", 40, "Software Engineer", 45000)
person = Person("Daniel", 22)
people = [student, employee, person]
for person in people:
    person.printMyself()









