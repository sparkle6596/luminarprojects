#algorithm=
#1=sort the given array
#2=low and upper variable declaration
#low=0,upper=len(lst)-1
#3=calc of mid of list
#mid=low+upper//2
# 3 condition:
#1.low=mid+1, search ele>mid
#2.upp=mid-1,search ele>mid
#3.elment=lst(mid):element found,search ele==mid
lst=[2,4,5,3,6,7,1,5]
element=int(input("enter a number"))
lst.sort()
low=0
upper=len(lst)-1
flag=0
while(low<=upper): #0<=7,7<=7,8<=7
       mid=low+upper//2 #0+7//2 ,7+7//2
       if (element>lst[mid]):#8>6 8>7
        low=mid+1 #0=6+1=7 #7+1=8

       elif(element<lst[mid]):#8<7
        upper=mid-1#7-1=6


       elif(element==lst[mid]):
           flag=1
if(flag>0):
    print("element found")
else:
    print("element not found")

