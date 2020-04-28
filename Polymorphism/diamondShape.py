class A: # Level 1
    def method(self):
        print("Class A method")

class B(A): # Level 2
    def method(self):
        print("This method belongs to class B")
    pass

class C(A): # Level 2
    def method(self):
        print("class C")
    pass

class D(B,C): # level 3
    # def method(self)
    pass

d= D()
d.method()
