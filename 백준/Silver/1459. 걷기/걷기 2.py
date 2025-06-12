import sys

x, y, w, s = map(int, sys.stdin.readline().split())

if (x + y) % 2 ==0:
    res1 = max(x, y) * s
else:
    res1 = (max(x, y) - 1) * s + w

res2 = (x + y) * w

res3 = min(x, y) * s + (abs(x - y)) * w
    
print(min(res1, res2, res3))
