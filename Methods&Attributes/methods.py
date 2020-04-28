# What are instance methods? Methods that make use of self parameter

class Employee:
    def employeeDetails(self):
        self.name = "Lalith"

    @staticmethod
    # Used when none of the attributes are sent as parameters
    def welcomeMessage():
        print("Welcome to our Organization")

e1 = Employee()
e1.employeeDetails()
print(e1.name)
e1.welcomeMessage()
