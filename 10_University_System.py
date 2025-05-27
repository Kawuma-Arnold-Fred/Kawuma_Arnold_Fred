class Person:
    def __init__(self, id_number, name, age):
        self.id_number = id_number
        self.name = name
        self.age = age
    
    def display_details(self):
        print(f'ID: {self.id_number}, Name: {self.name}, Age: {self.age}')

class Lecturer(Person):
    def __init__(self, id_number, name, age, department):
        super().__init__(id_number, name, age)
        self.department = department
    
    def display_details(self):
        super().display_details()
        print(f'Role: Lecturer, Department: {self.department}')

# Subclass: Student
class Student(Person):
    def __init__(self, id_number, name, age, program):
        super().__init__(id_number, name, age)
        self.program = program
    
    def display_details(self):
        super().display_details()
        print(f'Role: Student, Program: {self.program}')

# Subclass: Staff
class Staff(Person):
    def __init__(self, id_number, name, age, position):
        super().__init__(id_number, name, age)
        self.position = position
    
    def display_details(self):
        super().display_details()
        print(f'Role: Staff, Position: {self.position}')

# Create objects
lecturer = Lecturer('L031', 'Dr. Bob Stone', 34, 'Computer Science')
student = Student('S0213', 'Jerry Maguire', 17, 'Biology')
staff = Staff('ST0112', 'Billie Jean', 54, 'Librarian')

# Display details
lecturer.display_details()
print()
student.display_details()
print()
staff.display_details()