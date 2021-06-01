


import re

n=input("enter the num to validate")
x='\d{10}'#rule
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
