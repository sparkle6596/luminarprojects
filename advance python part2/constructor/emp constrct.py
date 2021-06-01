class Employee:
    def __init__(self,name,id,designation,company):
        self.name=name
        self.id=id
        self.designation=designation
        self.company=company
    def print(self):
        print(self.name,"\n",self.id,"\n",self.designation,"\n",self.company)
obj=Employee("anu",9,"hr man","luminar")
obj.print()


