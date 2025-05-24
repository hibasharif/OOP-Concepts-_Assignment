class Employee:
    """Class demonstrating Python's access modifiers (public, protected, private)"""
    
    def __init__(self, name, salary, ssn):
        """
        Initialize employee attributes with different access levels
        
        Args:
            name (str): Public employee name
            salary (float): Protected salary (shouldn't be accessed directly)
            ssn (str): Private social security number
        """
        self.name = name        # Public (no underscore)
        self._salary = salary   # Protected (single underscore)
        self.__ssn = ssn        # Private (double underscore - name mangled)

    def show_ssn(self):
        """Safe way to access private SSN (shows only last 4 digits)"""
        return f"XXX-XX-{self.__ssn[-4:]}"  # Can access __ssn inside class methods

# Usage
emp = Employee("Alice", 50000, "123-45-6789")

# 1. Public attribute - no restrictions
print(emp.name)        # Output: "Alice" (works)

# 2. Protected attribute - accessible but "private by convention"
print(emp._salary)     # Output: 50000 (works but violates convention)

# 3. Private attribute - direct access fails
# print(emp.__ssn)     # AttributeError: 'Employee' object has no attribute '__ssn'

# 4. Proper way to access private attribute
print("Safe SSN:", emp.show_ssn())  # Output: "XXX-XX-6789"

# 5. How Python actually stores private attributes (name mangling)
print("Mangled name access:", emp._Employee__ssn)  # Output: "123-45-6789" (but DON'T do this!)