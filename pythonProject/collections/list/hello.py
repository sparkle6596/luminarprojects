rows = int(input("Please Enter the Total Number of Rows  : "))


for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print('*', end = '  ')
    print()#rightangled triangle