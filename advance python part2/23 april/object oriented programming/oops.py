#used to create reusabilty
#class :design pattern eg:plan
#object : real world entity :house (so many)
#reference ,variable name as reference #objectine refer cheyyan
#each object has its their own reference(memmory location of a object)
#.........................................................................................................#



class Person:#start with caps
    def print(self,name,age,gender):#instance variable its a function or method (differentiate inside and outside function)of class
        self.name=name
        self.age=age
        self.gender=gender
        print("inside print",self.name,self.age,self.gender)
pe=Person()# pe is reference variable of class object
pe.print("anu",23,"female")

re=Person()
re.print("amal",4,"male")











