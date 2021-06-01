# def sub(num1,num2):
#     return num1-num2
#
# print(sub(10,2))


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def sub(num1,num2):
#     if num1<num2:
#         (num1,num2)=(num2,num1)
#     return num1-num2
# print(sub(2,10)) #do not return negatives
# #already define functnilekk features add cheyyan
#

#==========================================================================================================
def shuffle_values(func):
    def wrapper(no1,no2):
        if no1<no2:
            (no1,no2)=(no2,no1)
        return func(no1,no2)
    return wrapper

@shuffle_values

def sub(num1,num2):
    return num1-num2


@shuffle_values
def div(num1,num2):
    return num1/num2

print(div(5,10))
print(sub(2,10))





























