list = [1, 2, 3, 1, 2, 4, 5, 4, 6, 2]
print("List Before removing duplicates", list)
dupli_list = []

for i in list:
    if i not in dupli_list:
        dupli_list.append(i)

list = dupli_list

print("List After removing duplicates ", list)