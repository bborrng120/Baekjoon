import math
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()
inf = 1e9
d = [inf]*n
d[0] = 0

def check(st):
    if st == "B":
        return "O"
    elif st == "O":
        return "J"
    else:
        return "B"

for i in range(n):
    for j in range(i+1, n):
        next_s = check(s[i])
        if s[j] == next_s:
            d[j] = min(d[j], d[i] + pow(i-j,2))
            
if d[n-1] != inf:
    print(d[n-1])
else:
    print(-1)