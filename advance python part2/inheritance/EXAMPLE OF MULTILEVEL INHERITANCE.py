#person child parent student
#child&parent inherit person
#student class inherit child
class Person:
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printp(self):
        print(self.name,"\n",self.age,"\n",self.gender)
class Parent(Person):
    def detailsp(self,job,place,salary):
        self.job=job
        self.place=place
        self.salary=salary
    def printpa(self):
        print(self.job,"\n",self.place,"\n",self.salary)
class Child(Person):
    def detailsc(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
    def printc(self):
        print(self.name,"\n",self.age,"\n",self.roll)
class Student(Child):
    def detailss(self,name,age,division):
        self.name=name
        self.age=age
        self.division=division
    def prints(self):
        print(self.name,"\n",self.age,"\n",self.division)
obj4=Student()
obj4.detailss("anu",22,"5b")
obj4.prints()
obj4.detailsc("anna",23,5)
obj4.printc()
obj3=Child()
obj3.detailsc("arun",22,4)
obj3.printc()
obj3.detailsp("hr","ekm",3000)
obj3.printpa()
obj3.detaild("neethu",22,"female")
obj3.printp()