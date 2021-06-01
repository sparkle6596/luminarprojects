#single inheritance
class Person:#parent class or base class or super class
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def print(self):
        print(self.name,"\n",self.age,"\n",self.gender)
#create child class
class Student(Person):#child class or sub clss or derived clss
    def det(self,roll,school):
        self.roll=roll
        self.school=school
    def prints(self):
        print(self.roll,"\n",self.school)
#pe=Person()
#pe.details("anu",22,"female")
#pe.print()
st=Student()
st.det(6,"sngist")
st.prints()
st.details("ant",22,"female")
st.print()

