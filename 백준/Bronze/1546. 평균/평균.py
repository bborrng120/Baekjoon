import sys

n = int(sys.stdin.readline())
score = list(map(int,sys.stdin.readline().split()))
sums = 0
maxs = max(score)
for i in score:
    sums += i/maxs*100
print(sums/n)