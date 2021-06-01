class Person:#parent class or base class or super class
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def print(self):
        print(self.name,"\n",self.age,"\n",self.gender)
class Employee(Person):
    def empdetails(self,id,name,desgnation,salary):
        self.id=id
        self.name=name
        self.desgnation=desgnation
        self.salary=salary
    def printemp(self):
        print(self.id,"\n",self.name,"\n",self.desgnation,"\n",self.salary)
class Emp2(Employee):
    def emp2details(self,name,id,designation):
        self.name=name
        self.id=id
        self.designation=designation
    def empprint(self):
        print(self.name,"\n",self.id,"\n",self.designation)
ob=Emp2()
ob.emp2details("anu",601,"hrm")
ob.empprint()
ob.empdetails(45,"anna","hr",34000)
ob.printemp()
ob.details("arun",45,"female")
ob.print()