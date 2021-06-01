class Student:
    def __init__(self,name,roll,course,mark):
        self.name=name
        self.roll=roll
        self.course=course
        self.mark=mark
    def __str__(self):
        return self.name
lst=[]
f=open("student","r")
for l in f:
    data=l.rstrip("\n").split(",")
    print(data)
    name=data[0]
    roll=data[1]
    course=data[2]
    mark=data[3]
    obj=Student(name,roll,course,mark)
for i in lst:
    if i.mark>=200:
        print(i)
584171