class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18")
    else:
        print("Age is valid")

# Usage
try:
    check_age(15)
except InvalidAgeError as e:
    print(e)  # Age must be at least 18