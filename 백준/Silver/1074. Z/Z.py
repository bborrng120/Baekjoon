import sys

n, r, c = map(int, sys.stdin.readline().split())
v = 0

while n != 0:
    s = 2**(n-1)
    pm = 2**(2*n-2)
    
    if r < s and c < s:
        v += 0
    elif r < s and c >= s:
        v += pm
        c -= s
    elif r >= s and c < s:
        v += pm*2
        r -= s
    else:
        v += pm*3
        r -= s
        c -= s
        
    n -= 1
print(v)