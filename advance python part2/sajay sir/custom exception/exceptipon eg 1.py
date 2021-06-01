



expenses=[2300,1500,1700,1800]

month=int(input("enter mon to print element 1)jan 2)feb 3)march"))

try:
    print("expenses",expenses[month])

except Exception as e: #e is not default
    print(e.args)


