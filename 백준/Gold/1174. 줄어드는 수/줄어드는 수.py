from itertools import combinations
import sys

n = int(sys.stdin.readline())
num = [str(i) for i in range(10)]
l = []
for i in range(1,11):
    for j in combinations(num,i):
        l.append(int((''.join(sorted(j, reverse=True)))))
    l.sort()

if len(l)>=n:
    print(l[n-1])
else:
    print(-1)