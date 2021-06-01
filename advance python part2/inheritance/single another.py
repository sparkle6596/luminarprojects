class Person:#parent class or base class or super class
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def print(self):
        print(self.name,"\n",self.age,"\n",self.gender)
class Employee:
    def empdetails(self,id,name,desgnation,salary):
        self.id=id
        self.name=name
        self.desgnation=desgnation
        self.salary=salary
    def printemp(self):
        print(self.id,"\n",self.name,"\n",self.desgnation,"\n",self.salary)
ob=Person()
ob.details("anu",22,"female")
ob.print()
em=Employee()
em.empdetails(2,"anna","hr",4000)
em.printemp()
em.details("arun",23,"male")
em.print()
