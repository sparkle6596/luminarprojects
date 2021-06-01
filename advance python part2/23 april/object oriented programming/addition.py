class Addition:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        #s=num1+num2
        print(self.num1+self.num2)
ob=Addition()
a=int(input("enter a number"))
b=int(input("enter number2"))
ob.sum(a,b) #function call


