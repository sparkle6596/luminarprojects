#combination of lower case and upper case letters and ending with a number
import re
n=input("enter the num to validate")
x="([a-zA-Z]+\d{1}$)"#+means eathelm onnu varanam#* means vannillel illelm scn illa
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
