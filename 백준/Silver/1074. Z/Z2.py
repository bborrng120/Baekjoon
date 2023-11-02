import sys

n, r, c = map(int, sys.stdin.readline().split())
v = 0

while n != 0:
    n -= 1
    s = 2**(n)
    pm = 2**(2*n)
    
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
        
print(v)
