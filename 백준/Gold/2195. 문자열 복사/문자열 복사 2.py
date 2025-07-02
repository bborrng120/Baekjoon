import sys

s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()

ans = len(p)
i, k = len(p), len(p)-1

while k >= 0:
    if p[k:i] in s:
        k -= 1
    else:
        ans -= i-k-2
        i = k+1
        
ans -= i-k-2
        
print(ans)
