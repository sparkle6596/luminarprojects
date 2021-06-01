#finally block
#all situationsil work cheyyum
k=[1,2,3]
a=int(input("enter a index value"))

try:
    print(k[a])
except:
    print("exception occured")
finally:
    print("finally")