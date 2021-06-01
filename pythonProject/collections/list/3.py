lst=[3,4,8]
newlst=[]
sum=sum(lst)
print(sum)
for i in lst:
    newlst.append(sum-i)
print (newlst)