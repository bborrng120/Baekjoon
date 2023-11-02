from collections import deque
import sys

d = [0]*100001
dx = [-1,1,2]
n, m = map(int,sys.stdin.readline().split())

queue = deque()
queue.append(n)

while queue:
    x = queue.popleft()
    if x == m:
        print(d[x])
        break
    for i in range(3):
        if i == 2:
            nx = x * dx[i]
        else:
            nx = x + dx[i]
            
        if 0 <= nx <= 10**5:
            if d[nx] == 0:
                d[nx] = d[x] + 1
                queue.append(nx)