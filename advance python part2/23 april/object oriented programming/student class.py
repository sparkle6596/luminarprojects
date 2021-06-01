class Student:
    def setval(self,name,age,gender,id):
        self.name=name
        self.age=age
        self.gender=gender
        self.id=id
    def printval(self,department):
        self.department=department
        print(self.name,self.age,self.gender,self.id,self.department)
st=Student()
st.setval("anu",22,"female",101)
st.printval("mca")

