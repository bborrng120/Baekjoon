from collections import deque
import sys

wheel = []
ans = 0
inc = 1

for _ in range(4):
    wheel.append(deque(list(map(int, sys.stdin.readline().strip()))))
    
t = int(input())
for _ in range(t):
    n, d = map(int, sys.stdin.readline().split())
    n = n-1
    l, r = [n-1, True], [n+1, True]
    rotate = [0]*4
    rotate[n] = d
    
    while 0<=l[0]<4 or 0<=r[0]<4:
        if 0<=l[0]<4 and l[1]:
            if wheel[l[0]][2] != wheel[l[0]+1][6]:
                rotate[l[0]] = -rotate[l[0]+1]
            else:
                l[1] = False
        if 0<=r[0]<4 and r[1]:
            if wheel[r[0]][6] != wheel[r[0]-1][2]:
                rotate[r[0]] = -rotate[r[0]-1]
            else:
                r[1] = False
                
        l[0] -= 1
        r[0] += 1
        
    for i in range(4):
        wheel[i].rotate(rotate[i])
        
for i in range(4):
    ans += wheel[i][0]*inc
    inc *= 2
    
print(ans)