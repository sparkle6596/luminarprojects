ls=[]
odd=[]
even=[]
for i in range(1,101):
    ls.append(i)
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(ls)
print(odd)
print(even)

