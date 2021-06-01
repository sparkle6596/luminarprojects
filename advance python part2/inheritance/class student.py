class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def printval(self):

        print("/n",self.name,"\n",self.roll)



    def __str__(self):
        return  self.name
f=open("student",'r')
for line in f:
    data=line.rstrip("\n").split(",")
    print(data)
    name=data[0] #because the name is in 0 th position of the list
    roll=data[1] #age is in 1th position
    obj=Student(name,roll)
    print(obj)
    obj.printval()