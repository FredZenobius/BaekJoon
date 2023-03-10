homework = []
a = 0
for i in range(28) : 
    a = int(input())
    homework.append(a)
homework.sort()
for i in range(30) :
    if i+1 not in homework :
        print(i+1)
        