class Employee:
    def initializeWorkingHours(self):
        self.numberOfWorkingHours = 40

    def displayWorkingHours(self):
        print(self.numberOfWorkingHours)

class Trainee(Employee):
    def initializeWorkingHours(self):
        self.numberOfWorkingHours = 50

    def resetNumberOfWorkingHours(self):
        super().initializeWorkingHours()

emp = Employee()
trainee = Trainee()

emp.initializeWorkingHours()
print("Number of Working Hours: ", end =' ')
emp.displayWorkingHours()

trainee.initializeWorkingHours()
print("Number of Working Hours: ", end =' ')
trainee.displayWorkingHours()

trainee.resetNumberOfWorkingHours()
print("Number of Working Hours: ", end =' ')
trainee.displayWorkingHours()
