# check if weekly target is achieved

class Employee:
    # class attributes
    name = "Ben"
    designation = "Sales executive"
    salesMadeThisWeek = 6

    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target achieved")
        else:
            print("NOPE!")


employeeOne = Employee()
employeeOne.hasAchievedTarget()
# Experimentation
# print(employeeOne.name )
#
# numbers = [1,2,3]
# print(type(numbers))
# print(type(employeeOne))
