number_list = []
a = list(map(int,input().split()))
count = a[0]
find_num = a[1]

number_list = list(map(int,input().split())) 

for i in number_list :
    if i < find_num :
        print(i, end=' ')
