line="hai hello hai hello"
words=line.split(" ")
dic={}

for i in words:
    if i not in dic:
        dic[i]=1
    elif i  in dic:
        dic[i]+=1
print(dic)




