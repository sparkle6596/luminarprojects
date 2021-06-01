#minimum lenth 8 and max15,except number
import re
n=input("enter")
x='(\D{8,15})'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
