#book name#author name#pagesm
class Book:
    def details(self,name,author,pages):
        self.name=name
        self.author=author
        self.pages=pages
    #def print(self):
        print("\n","name:",self.name,"\n","author:",self.author,"\n","pages:",self.pages)
    def __str__(self):#to string method only return# string eg="name"
        return self.name+self.author+str(self.pages)#convert int to string
ob=Book()
ob.details("abc","xyz",79)
#ob.print()
print(ob)