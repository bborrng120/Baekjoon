import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
fixed = []
d = [1]*(n+1)

for _ in range(m):
    fixed.append(int(input()))
    
for i in range(2,n+1):
    d[i] = d[i-2]+d[i-1]
    
prev = 0
ans = 1
for i in fixed:
    ans *= d[i-prev-1]
    prev = i
ans *= d[n-prev]

print(ans)