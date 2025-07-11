import sys

n, k = map(int, sys.stdin.readline().split())
ans = -1

while n <= k:
    temp = k
    if k%2 != 0:
        k -= 1
    else:
        k //= 2
    ans += 1
    
print(ans+temp-n)
