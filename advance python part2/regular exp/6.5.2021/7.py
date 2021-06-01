#KERALA regestration numbers
import re


n = input("enter")
x = "([k][L]\d{2}[A-Z]\d{4}$)"
match =re.fullmatch(x, n)
if match is  not None:
    print("valid")
else:
    print("invalid")
