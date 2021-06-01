class Employee:
    company="luminar"#static variable
    def setval(self,name,id,age,designation,salary):
        self.name=name#instance variable
        self.id=id
        self.age=age
        self.designation=designation
        self.salary=salary
    def printval(self):
        print(self.name)
        print(self.id)
        print(self.age)
        print(self.designation)
        print(self.salary)
        print(Employee.company)
emp=Employee()
emp.setval("neethu",101,25,"hr",4000)
emp.printval()
#2 types of variables
# #instance -related to methods ,called using self key word
# #static variable -related to class,called using class name
