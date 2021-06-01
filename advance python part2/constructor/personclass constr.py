class Person:
    def __init__(self,name,age):#constructor =initialisation,automatically invoke when object created
        self.name=name
        self.age=age
    def printval(self,gender):
        self.gender=gender
        print(self.name,"\n",self.age,"\n",self.gender)
ob=Person("anu",22)
ob.printval("female")
