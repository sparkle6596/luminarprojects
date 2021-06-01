#add


#def add(num1,num2):#parameters
    #return num1+num2
#res=add(10,20)#arguments,actual values
#print(res)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def add(*args):
    res=0
    for num in args:#it will accept any number of arguments in the form of tuple
        res+=num
    return res

print(add(10,3,5,10))


def print_employee(**kwargs):#key value pairs accept as dictionary
    for k,v in kwargs.items():
        print(k,"=",v)


print_employee(id=100,place="trissur",item="kakkanad")




def print_employe(**kwars):
    print(kwars)
print_employe(id=100,name="ambily",salary=2500)




employees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    1001: {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    1003: {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

}


def print_employe(**kwargs):





print_employe(id=1000)















