
#filter returns objects
lst=[7,9,8,6]
def check_even(number):
    return number%2==0


even=list(filter(lambda number:number%2==0,lst))
print(even)

#filter number>5


num=list(filter(lambda number:number>5,lst))
print(num)


employees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]


developers=list(filter(lambda emp:emp["designation"]=="developer",employees))
print(developers)

#oues:emp names of designation is developer


#developers=list(filter(lambda emp:emp["designation"]=="developer",employees))
#developers_name=list(map(lambda emp:emp["name"],developers))
#print(developers_name)


#both in one(map,and filter)

developers_name=list(map(lambda emp:emp ["name"],list(filter(lambda emp:emp["designation"]=="developer",employees))))
print(developers_name)



