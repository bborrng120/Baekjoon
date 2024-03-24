from itertools import combinations
import sys

n = int(sys.stdin.readline())
num = [str(i) for i in range(10)]
ans = []
for i in range(1,11):
    for j in combinations(num,i):
        ans.append(int(''.join(sorted(j,reverse=True))))
        
ans.sort()
if len(ans)>n:
    print(ans[n])
else:
    print(-1)