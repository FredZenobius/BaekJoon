number_list = []
count = input()

number_list = list(map(int,input().split())) 
print(min(number_list), max(number_list), sep=' ')