#map functn(),oro objectinum corresponding output venam ennundel we use map(),applicable in list
#filter,particular itemsnu maathram output,conditional base checking,applicable in list
#reduce


lst=[2,3,4,5,6,7]
#squares of all object
sq=list(map(lambda num:num**2,lst))#covert to list otherwise it returns location
print(sq)

names=["ajay","amal"]
upp=list(map(lambda name:name.upper(),names))
print(upp)




employees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]
#print employee name
emp_names=list(map(lambda emp:emp["name"],employees))
print(emp_names)

emp_sal=list(map(lambda emp:emp["salary"],employees))
print(emp_sal)

#print all employee s whos desgnation ==developer

#def emplo_developer(emp):
    #return emp["designation"]=="developer"


developers=list(filter(lambda emp:emp["designation"]=="developer",employees))
print(developers)

