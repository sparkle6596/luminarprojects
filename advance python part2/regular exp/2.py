import re
count=0
matcher=re.finditer('ab','abbbab')
for match in matcher:
    print("match available at",match.start())#used to find which index matching is available#position
    print("group",match.group())#which goup we search
    count+=1
print("count",count)

