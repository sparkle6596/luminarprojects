num1=float(input("enter number1"))
num2=float(input("enter number2"))
choice=(input("enter your choice"))
def add(num1,num2):
    sum=num1+num2
    print(sum)
def sub(num1,num2):
    sub=num1-num2
    print(sub)
def mul(num1,num2):
    mul=num1*num2
    print(mul)
def division(num1,num2):
    division=num1/num2
    print(division)
if(choice=='+'):
    add(num1,num2)
elif(choice=='-'):
    sub(num1,num2)
elif(choice=='*'):
    mul(num1,num2)
elif(choice=='/'):
    division(num1,num2)
else:
    print("invalid")




