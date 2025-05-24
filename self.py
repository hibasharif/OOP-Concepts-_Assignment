class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Usage
student = Student("Alice", 95)
student.display()