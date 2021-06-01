import re
count=0
matcher=re.finditer('ab','abbbab')
for match in matcher:
    count+=1
print("count",count)

