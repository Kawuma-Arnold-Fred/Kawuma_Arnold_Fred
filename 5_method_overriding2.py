class University_Employee:
    def emp_role(self):
        print('Works at University.')
        
class Lecturer(University_Employee):
    def emp_role(self):
        print('Teaches Students')
        
class Security_Guard(University_Employee):
    def emp_role(self):
        print('Manages access into university')
        
def role_Executer(employee):
    employee.emp_role()
    
Gerald = Lecturer()
Mark = Security_Guard()

Gerald.emp_role()
Mark.emp_role()