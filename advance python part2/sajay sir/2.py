employees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    1001: {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    1003: {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},
}
#nested dictionary

def print_employe(**kwargs):#_because of coding standard,ethra argumnts venelm accept cheyyam(88kwargs)
    id=kwargs["id"]#kwargsil eid variable eduth vachu,eid=1003
    prop=kwargs["prop"]
    if id in employees:
        print(employees[id]["name"])
        print(employees[id]["salary"])
        print(employees[id]["designation"])
    else:
        print("invalid")

print_employe(id=1003,prop="salary",porp="designation")



