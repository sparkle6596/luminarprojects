f=open("next","r")
dic={}#created a empty dictionary to append the word to the dict
for i in f:#iterate the f into i
    # print(i)
    word=i.rstrip("\n").split(" ") #split the whole words
    # print(word)
    for a in word: # the iterate the words in to a a
        if a not in dic:# then the a is not in dictionary
            dic[a] = 1#then add the words
        elif a in dic:#suppose words in dictionary
            dic[a] += 1#then increament by 1
#print(dic)# print that dictionary
for k,v in dic.items():
    print(k,",",v)


