class Employee:
    # Class attributes
    numberOfWorkingHours = 40

e1 = Employee()
e2 = Employee()
# Instance attributes
# Instance attributes are checked for initially and then Class attributes
e1.numberOfWorkingHours = 45

print(e1.numberOfWorkingHours)
print(e2.numberOfWorkingHours)
