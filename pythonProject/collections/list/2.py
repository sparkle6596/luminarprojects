lst=[1,2,3,4,5,6,7,8,9]
element=int(input("enter a number"))
for i in lst:
     for j in lst:
        if(i+j==element):
          print(i,j)