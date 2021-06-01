lst=[1,2,3]
# find squres
squares=[num**2 for num in lst]
print(squares)

fruits=["apple","orange","mango"]
pairs=[ (fruits,fruits) for f in fruits]
print(pairs)

lst1=[10,20]
lst2=[30,40]
pairs_lst=[(num1,num2)for num1 in lst1 for num2 in lst2]#return cheyandath left
print(pairs_lst)

#print evens

evens=[num for num in lst if num%2==0]#return cheyyandath left
print(evens)



lst=[7,8,9,4,3,2]
#num>5 num+1,num<5 num-1
op=[number+1 if number>5 else number-1 for number in lst ]#return cheyyandath left kodukkuka
print(op)



employees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]


employees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]

#print employee names whose designation is developer

developers=[ emp for emp in employees if ["designation"]=="developer"]#condition check in right side
print(developers)

#highest salary

sal=max([emp["salary"] for emp in employees ])
print(sal)