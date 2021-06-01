import re

n=input("enter email")
x='^[a-z0-9_.+-]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")