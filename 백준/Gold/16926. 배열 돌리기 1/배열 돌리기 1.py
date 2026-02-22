import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())
my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for k in range(min(n,m)//2):
    q = deque()
    
    for j in range(k, m-k-1):
        q.append(my_list[k][j])
    for i in range(k, n-k-1):
        q.append(my_list[i][m-k-1])
    for j in range(m-k-1, k, -1):
        q.append(my_list[n-k-1][j])
    for i in range(n-k-1, k, -1):
        q.append(my_list[i][k])
        
    c_len = (m-2*k) * 2 + ((n-2*k)-2) * 2
    q.rotate(-(r%c_len))
    
    for j in range(k, m-k-1):
        my_list[k][j] = q.popleft()
    for i in range(k, n-k-1):
        my_list[i][m-k-1] = q.popleft()
    for j in range(m-k-1, k, -1):
        my_list[n-k-1][j] = q.popleft()
    for i in range(n-k-1, k, -1):
        my_list[i][k] = q.popleft()
        
for i in my_list:
    print(*(i))