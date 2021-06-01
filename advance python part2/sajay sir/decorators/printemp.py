def admin_required(fun):
    def wrapper(user,pin):
        if user!="admin":
            raise Exception("not eligible")
        else:
            return fun(user,pin)
    return wrapper


@admin_required

def change_pin(user,pin):
    mypin=pin
    return pin

@admin_required

def delete_pin(user,account):
    return str(account)+"deleted"



print(change_pin("admin",1000))
print(delete_pin("admin",1000))