dic="abcdbca"
rec={}
for i in dic:
    if i not in rec:
        rec[i]=1
    else:
        print(i)
        break
