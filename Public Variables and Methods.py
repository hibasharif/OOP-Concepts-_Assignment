class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} started!")

# Usage
car = Car("Toyota")
print(car.brand)
car.start()