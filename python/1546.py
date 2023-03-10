subject = int(input())
score = list(map(float,input().split()))
bestScore = max(score)

for i in range(subject) :
    score[i] = score[i] / bestScore * 100

print(sum(score) / subject)