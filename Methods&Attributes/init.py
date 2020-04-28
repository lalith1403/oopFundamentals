#
class Employee:
    def __init__(self, name):
        self.name = name

    def enterEmployeeDetails(self):
        self.name = "Mark"

    def displayEmployeeDetails(self):
        print(self.name)

name = "Lalith"
# without init method, this function call results in an error.
e1 = Employee("Narayan")
e1.displayEmployeeDetails()
e2 = Employee(name)
e2.displayEmployeeDetails()
