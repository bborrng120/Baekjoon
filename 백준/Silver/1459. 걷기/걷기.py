import sys

x, y, w, s = map(int, sys.stdin.readline().split())

if w >= s:
    if (x + y) % 2 ==0:
        res = max(x, y) * s
    else:
        res = (max(x, y) - 1) * s + w
elif w*2 < s:
    res = (x + y) * w
else:
    res = min(x, y) * s + (abs(x - y)) * w
    
print(res)