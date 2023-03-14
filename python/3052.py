num_list = []
remain_list = []
for i in range(10) :
    a = int(input())
    num_list.append(a)
for i in range(10) :
    a = num_list[i]%42
    if a not in remain_list :
        remain_list.append(a)
print(len(remain_list))