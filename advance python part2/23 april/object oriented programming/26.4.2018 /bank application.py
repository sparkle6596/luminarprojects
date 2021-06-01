class Bank:
    bankname="hdfc"
    def account(self,name,accountype):
        self.name=name
        self.accountype=accountype
        self.minbal=500
        self.balance=self.minbal
        print(self.name)
        print(self.accountype)
        print(Bank.bankname)
    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        print("your",Bank.bankname,"credited with",self.amount)
        print("current balance",self.balance)
    def withdraw(self,wamount):
        self.wamount=wamount
        if self.wamount>self.balance:
            print("insufficient bal")
        else:

            print("avail balance",self.balance-self.wamount)
obj=Bank()
obj.account("anu","fixed")
obj.deposit(2500)
obj.withdraw(1000)








