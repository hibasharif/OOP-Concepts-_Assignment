#callable() and __call__()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return self.factor * x

# Usage
mul = Multiplier(3)
print(callable(mul))  # True
print(mul(5))        # 15