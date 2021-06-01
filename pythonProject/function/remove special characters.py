a="hello ;;..world"
b=""
c=".;:/"
for i in a:
    if(i not in c):
        b+=i
print(b)