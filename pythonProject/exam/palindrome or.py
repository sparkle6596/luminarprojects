n= int(input("Enter the Strating number "))
m= int(input("Enter the Ending number "))
for i in range(n,m):
    temp = i
    rev=0
    while(i>0):
        div=i%10
        rev=rev*10+div
        i=i//10
    if(temp==rev):
        print(temp,"The number is a Palindrom")
    else:
        print(temp,"The number is not a Palindrom")
