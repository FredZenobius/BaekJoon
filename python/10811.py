nmNum = list(map(int,input().split()))
basket = []
for i in range(nmNum[0]) :
    basket.append(i+1)
for i in range(nmNum[1]) :
    reverseNum = list(map(int,input().split()))
    reverseBasket = []
    for j in range(reverseNum[0]-1, reverseNum[1]):
        reverseBasket.append(basket[j])
    reverseBasket.reverse()
    for j in reverseBasket :
        basket.remove(j)
    basket[reverseNum[0]-1:reverseNum[0]-1] = reverseBasket
    
print(*basket)