#Aggregation 
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employee=None):
        self.name = name
        self.employee = employee

# Usage
emp = Employee("Alice")
dept = Department("HR", emp)
print(dept.employee.name)  # Alice