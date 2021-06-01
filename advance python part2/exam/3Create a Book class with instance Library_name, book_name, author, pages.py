#Create a Book class with instance Library_name, book_name, author, pages

class Book:
    def about(self,Library_name, book_name, author, pages):
        self.Library_name=Library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
        print(self.Library_name,"\n",self.book_name,"\n",self.author,"\n",self.pages)
obj=Book()
obj.about("aham","neelakasham","madhavi",456)