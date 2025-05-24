class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# Usage
d = D()
d.show()  # B (due to MRO: D -> B -> C -> A)
print(D.mro())  # Shows method resolution order