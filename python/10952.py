number_list = []
a = []
while True:
    a = list(map(int,input().split())) 
    if a[-1] == 0 and a[-2] == 0 :
        break
    else :
        number_list += a
# print(number_list)
for i in range(1, int(len(number_list)/2+1)) :
    print(number_list[i*2-1] + number_list[i*2-2])