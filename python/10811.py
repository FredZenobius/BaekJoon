nmNum = list(map(int,input().split()))
basket = []
for i in range(nmNum[0]) :
    basket.append(i+1)
for i in range(nmNum[1]) :
    reverseNum = list(map(int,input().split()))
    reverseBasket = []
    for i in range(reverseNum[0]-1, reverseNum[1]):
        reverseBasket.append(basket[i])
    print(*reverseBasket)
    reverseBasket.reverse()
    print(*reverseBasket)
    for j in range(reverseNum[0]-1, reverseNum[1]) :
        del basket[reverseNum[0]]
    basket[reverseNum[0]:reverseNum[0]] = reverseBasket
    
print(*basket)