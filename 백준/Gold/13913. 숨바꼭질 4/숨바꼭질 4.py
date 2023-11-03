from collections import deque
import sys

d = [-1]*100001
my_list = [0]*100001
dx = [2,1,-1]
n, m = map(int,sys.stdin.readline().split())
q = deque([(n,0)])
d[n] = 0

while q:
    x,count = q.popleft()
    if x == m:
        break
    for i in range(3):
        if i==0:
            nx = x*dx[i]
        elif i==1 or i==2:
            nx = x+dx[i]
        if 0<=nx<100001 and d[nx] == -1:
            q.append((nx,count+1))
            my_list[nx] = x
            d[nx] = d[x]+1
print(d[m])

k = m
ans = [k]
while k != n:
    ans.append(my_list[k])
    k = my_list[k]
print(*ans[::-1])