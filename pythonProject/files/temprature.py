f=open("/home/ambily/Temperature","r")
dic={}
for i in f:
    word = i.rstrip("\n").split(" ")
    if(word[0] not in dic):
        year=word[0]
        dic[year]=word[1]
    else:
        year=word[0]
        temp=int(word[1])
        if(int(dic[year])<temp):
            dic[year]=str(temp)
for i in dic:
    print(i,":",dic[i])

