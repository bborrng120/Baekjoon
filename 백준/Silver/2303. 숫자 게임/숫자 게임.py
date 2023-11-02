from itertools import combinations
import sys

n = int(sys.stdin.readline())
card = []
ans = []
for _ in range(n):
    t = list(map(int,sys.stdin.readline().split()))
    card.append(t)

for i in card:
    maxs = 0
    for j in list(combinations(i,3)):
    	s = str(sum(j))
    	maxs = max(maxs,int(s[-1]))
    ans.append(maxs)

maxa = 0
for i in range(len(ans)):
    if ans[i] > maxa:
    	maxa = ans[i]
    	res = i+1
    elif ans[i] == maxa:
    	res = i+1
        
print(res)