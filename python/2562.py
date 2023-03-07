number_list = []
a = 0
for i in range(9) :
    a = int(input())
    number_list.append(a)

maxValue = max(number_list)
print(maxValue)

for i in range(9): #number.index(maxValue)+1로 최대값의 순서를 구할 수도 있다.
    if number_list[i] == maxValue :
        print(i+1)