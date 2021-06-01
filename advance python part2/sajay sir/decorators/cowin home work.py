def decorator(fun):
    def wrapped(name,age,health_issues,place):
        if (age>65) or (health_issues==True):
            print("request is allowed to ekm")
        else:
            raise Exception("not eligible")
            return fun(name,age,place,health_issues)
    return wrapped



@decorator
def vaccination_portal(**kwargs):
    name=kwargs["name"]
    age=kwargs["age"]
    place=kwargs["place"]
    health_issues=kwargs["health_issues"]
vaccination_portal(name="ram",age=80,place="ekm",health_issues=False)















