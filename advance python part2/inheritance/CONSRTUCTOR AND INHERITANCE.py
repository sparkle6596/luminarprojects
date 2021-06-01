class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name",self.name)
        print("age",self.age)
class Student(Person):
    def __init__(self,roll,mark,name,age):
        super().__init__(name,age)
        self.roll=roll
        self.mark=mark
        #
       # print(self.age)
    def print(self):
        print("roll",self.roll)
        print("mark",self.mark)
cr=Student(2,4,"anu",23)
cr.printval()
cr.print()
