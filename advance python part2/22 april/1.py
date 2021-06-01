#global variable
a=2
def printa():
    global a#function nte outside variable
    print(a)
    a=a+2#local variable
printa()
print(a)