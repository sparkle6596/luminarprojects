class Employee:
    def detail(self,name,id,number,depa):
        self.name=name
        self.id=id
        self.number=number
        self.depa=depa
    #def printm(self):
        print("\n",self.name,"\n",self.id,"\n",self.number,"\n",self.depa)
    def __str__(self):
        return self.name+str(self.id)
ob=Employee()
ob.detail("annu",34,897535678,"hr")
print(ob)