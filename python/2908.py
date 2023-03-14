numList = list(map(str,input().split()))
reversenum = ['','']
for i in range(len(numList)) :
    for j in numList[i] :
        reversenum[i] = j + reversenum[i]
for i in range(len(reversenum)) :
    reversenum[i] = int(reversenum[i])
if reversenum[0] > reversenum[1] :
    print(reversenum[0])
else :
    print(reversenum[1])
