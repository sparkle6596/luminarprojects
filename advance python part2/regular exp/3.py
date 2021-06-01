#rules 1
import re
x="[abc]"#either a,b or c
m=re.finditer(x,"abbfgnbnhabcece")
for n in m:
    print(n.start())
    print(n.group())