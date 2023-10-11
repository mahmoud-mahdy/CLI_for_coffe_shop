order = [1,2,3,1,2,3,1,2,3,4]
max_e = 2
count = {}
list = []
for i in order:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
    if max_e >= count[i]:
        list.append(i)
print(list)