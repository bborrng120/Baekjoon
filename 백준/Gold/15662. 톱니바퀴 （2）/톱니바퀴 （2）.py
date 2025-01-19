from collections import deque
import sys

wheel = []
ans = 0

t = int(sys.stdin.readline())
for _ in range(t):
    wheel.append(deque(list(map(int, sys.stdin.readline().strip()))))
    
k = int(input())
for _ in range(k):
    n, d = map(int, sys.stdin.readline().split())
    n = n-1
    l, r = [n-1, True], [n+1, True]
    rotate = [0]*t
    rotate[n] = d
    
    while 0<=l[0]<t or 0<=r[0]<t:
        if 0<=l[0]<t and l[1]:
            if wheel[l[0]][2] != wheel[l[0]+1][6]:
                rotate[l[0]] = -rotate[l[0]+1]
            else:
                l[1] = False
        if 0<=r[0]<t and r[1]:
            if wheel[r[0]][6] != wheel[r[0]-1][2]:
                rotate[r[0]] = -rotate[r[0]-1]
            else:
                r[1] = False
                
        l[0] -= 1
        r[0] += 1
        
    for i in range(t):
        wheel[i].rotate(rotate[i])
        
for i in range(t):
    ans += wheel[i][0]
    
print(ans)