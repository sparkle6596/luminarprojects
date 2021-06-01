class Person:
    def details(self,name,age,phno):
        self.name=name
        self.age=age
        self.phno=phno
        print(self.name,"\n",self.age,"\n",self.phno)

class Student1(Person):
    def about(self,gender,rollno):
        self.gender=gender
        self.rollno=rollno
        print(self.gender,"\n",self.rollno)
class Student2(Person):
    def det(self,div,place):
        self.div=div
        self.place=place
        print(self.div,"\n",self.place)
class Student3(Student1,Person):
    def deta(self,grade,status):
        self.grade=grade
        self.status=status
        print(self.grade,"\n",self.status)
object = Student3()
object.details("anu",22,45690987633)
object.about("female",6)
object.deta("a+","ecxelent")
obj=Student2()
obj.det("5b","chalakudy")





