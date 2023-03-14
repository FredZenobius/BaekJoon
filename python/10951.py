number_list = []
a = []
while True:
    try:
        a = list(map(int,input().split())) 
        number_list += a
    except Exception as e :
        break
# print(number_list)
for i in range(1, int(len(number_list)/2+1)) :
    print(number_list[i*2-1] + number_list[i*2-2])