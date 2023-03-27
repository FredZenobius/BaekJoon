num = int(input())
for i in range(num) :
    for j in range(num-1, 0, -1) :
        if j > i:
            print(end=' ')
    for j in range((i+1)*2-1) :
        print(end='*')
    print()
for i in range(num-2, -1, -1) :
    for j in range(num) :
        if j > i:
            print(end=' ')
    for j in range((i+1)*2-1):
        print(end='*')
    print()