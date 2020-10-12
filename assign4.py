list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

for ele in list1:
    if ele < 0:
        list1.remove(ele)

for ele in list2:
    if ele < 0:
        list2.remove(ele)

print("Output:", (list1))
print("Output:", (list2))
