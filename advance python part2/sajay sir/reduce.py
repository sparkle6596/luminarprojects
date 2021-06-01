#reduce in functools,single values aan output enkil we use reduce,like sum of the list

import functools
lst=[2,3,4,5]
total=functools.reduce(lambda num1,num2:num1+num2,lst)
print(total)


#highest  value

high=functools.reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)#num1 and num2 are arguments
print(high)


