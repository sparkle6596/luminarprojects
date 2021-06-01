class Student:
    def __init__(self,name,roll,department,mark):
        self.name=name
        self.roll=roll
        self.department=department
        self.mark=mark
    def printval(self):
        print(self.name,"\n",self.roll,"\n",self.department,"\n",self.mark)


    def __str__(self):
        return self.name
lst=[]
f=open("STUDENT",'r')
for line in f:
    data=line.rstrip("\n").split(",")
    print(data)
    name=data[0]
    roll=data[1]
    department=data[2]
    mark=int(data[3])
    ob=Student(name,roll,department,mark)
    lst.append(ob)
for i in lst:
    if i.mark>190:
        print(i)
#
#
#
#
#
