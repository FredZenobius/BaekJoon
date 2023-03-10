nmNum = list(map(int,input().split()))
basket = []
for i in range(nmNum[0]) :
    basket.append(i+1)
for j in range(nmNum[1]) :
    change_order = list(map(int,input().split()))
    basket[change_order[0]-1], basket[change_order[1]-1] = basket[change_order[1]-1], basket[change_order[0]-1]
    change_order.clear()

print(*basket)