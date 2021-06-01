#fifo
#operations insertion and deletion
que= []#empty list
size=int(input("enter the size"))
frond=0#start from 0
rear=0#last element
n=0
def insert():
    global frond,rear,size,que
    if rear>=size:
        print("que is full")
    else:
        p=int(input("enter the element want to insert::"))
        que.insert(rear,p)
        rear+=1
        for i in range(frond,rear):
            print(que[i])
def delete():
    global frond,rear,size,que
    if rear==frond:
        print("que is empty")
    else:
        frond+=1
        for i in range(frond,rear):
            print(que[i])
while n!=1:
    print("...... enter operation")
    opt=int(input("press\n1)insert\n2)delete\n"))
    if opt==1:
        insert()
    elif opt==2:
        delete()












