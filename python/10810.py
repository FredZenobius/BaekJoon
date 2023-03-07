nmValue = list(map(int,input().split()))
order = []
basket = []

for i in range(nmValue[0]) :
    basket.append(0)

for i in range(nmValue[1]) :
    order = list(map(int,input().split()))    
    for j in range(order[0]-1, order[1]) :
        basket[j] = order[2]

print(*basket)

