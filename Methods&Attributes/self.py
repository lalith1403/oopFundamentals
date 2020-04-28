class Employee:
    def employeeDetails(self):
        self.name = "Lalith"
        print("Name: ",self.name)
        self.age = 22

    def printEmployeeDetails(self):
        print("Printing in a new method")
        print("Name: ", self.name)
        print("Age: ", self.age)

e1 = Employee()
e1.employeeDetails()  # is equivalent to Employee.employeeDetails(e1)
print(e1.age)
e1.printEmployeeDetails()
