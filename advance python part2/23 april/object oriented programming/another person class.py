class Person:
    def setval(self,name,age):
        self.name=name
        self.age=age
    def printval(self,gender):
        self.gender=gender
        print(self.name,self.age,self.gender)
ob=Person()
ob.setval("anu",22)
ob.printval("female")
