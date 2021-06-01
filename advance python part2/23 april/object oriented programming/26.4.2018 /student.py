class Student:
    school="sngist"
    def setval(self,name,age,standard,rollno):
        self.name=name
        self.age=age
        self.standard=standard
        self.rollno=rollno
    def printval(self):
        print("name:",self.name)
        print("age:",self.age)
        print("standard:",self.standard)
        print("rollno:",self.rollno)
        print("school:",Student.school)
stu=Student()
stu.setval("anu",12,"5b",1)
stu.printval()

