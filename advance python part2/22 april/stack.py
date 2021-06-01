#used to store data
#stack -adding process is called push
# lifo
# #removing-pop

stack = []#empty list
size=int(input("enter the size"))
top=0#start from 0
n=0
def push():
    global top,size
    if top>=size:
        print("stack is full")
    else:
        p=int(input("enter the element want to push"))
        stack.append(p)
        top+=1
        print(stack)
def pop():
    global top,size
    if top<=0:
        print("stack is empty")
    else:
        stack.pop()
        top-=1
        print(stack)
while n!=1:#for repeat the options
    print("......enter the operation want to perform")
    opt=int(input("press::1)push 2)pop"))
    if opt==1:
        push()
    elif opt==2:
        pop() 952578



