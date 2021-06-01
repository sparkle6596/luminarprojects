class Animal:
    def _init_(self,breed,age):
        self.breed=breed
        self.age=age
    def printval(self):
        print(self.breed)
        print(self.age)
class Dog(Animal):
    def _init_(self,color,breed,age):
        super()._init_(breed,age)
        self.color=color
    def print(self):
        print(self.color)
        print(self.breed,self.age)
obj=Dog("black","boxer",3)
obj.printval()
obj.print()