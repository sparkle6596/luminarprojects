f=open("/home/ambily/customer","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    data1=data[4]
    if data[4] not in dic:
        dic[data[4]]=1
    else:
        dic[data[4]]+=1
print(dic)
    #print(data1)

    #data=i.rstrip("\n").split(",")
    #for a in data:

    #fname=data[1]
    #age=data[3]
    #cou=data[-1]
    #list=([fname,age,cou])#add the items into a list
    #for a in list:



