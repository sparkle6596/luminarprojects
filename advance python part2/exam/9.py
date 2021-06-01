import re
n=input("enter")
x="[A-Z]+[a-z]+$"
matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("not valid")