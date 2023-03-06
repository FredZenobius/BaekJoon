case_count = input()
case_list = [ ]
for i in range(int(case_count)) : 
    case_list += list(map(int,input().split())) 

# print(case_list)
for i in range(1,(int(case_count)+1)) :
    print("Case #" + str(i) + ":" , str(int(case_list[i*2-1]) + int(case_list[i*2-2])))