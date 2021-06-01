
import re
n=input("enter the num to validate")
x='{+}{9}{1}\d{10}'
matche=re.finditer(x,n)
if matche is not None:
    print("valid")
else:
    print("invalid")
