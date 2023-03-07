number_list = []
count = int(input())
count = 0
number_list = list(map(int,input().split())) 
find_num = int(input())

for i in number_list :
    if i == find_num :
        count += 1

print(count)