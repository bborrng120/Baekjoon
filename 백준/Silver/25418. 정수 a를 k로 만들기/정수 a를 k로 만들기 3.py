import sys

n, k = map(int, sys.stdin.readline().split())
ans = 0

while n < k:
    if k%2 == 0 and k//2 >= n:
        k //= 2
    else:
        k -= 1
    ans += 1
    
print(ans)
