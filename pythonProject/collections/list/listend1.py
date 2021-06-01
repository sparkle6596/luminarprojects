ls=[]
flag=0
for i in range(1,101):
    ls.append(i)
for i in ls:
    for j in range(2,101):
        if(i%j==0):
            flag=1
