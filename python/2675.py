count = int(input())

for i in range(count) :
    order_list = list(map(str,input().split()))
    for j in order_list[1] :
        for k in range(int(order_list[0])) :
            print(j, end='')
        print()