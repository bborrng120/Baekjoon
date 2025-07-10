from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
q = deque([(n, 0)])
visited = [0]*(k+1)

while q:
    a, c = q.popleft()
    
    if a == k:
        print(c)
        break
    
    if a+1 <= k:
        if not visited[a+1]:
            q.append((a+1, c+1))
            visited[a+1] = 1
    if a*2 <= k:
        if not visited[a*2]:
            q.append((a*2, c+1))
            visited[a*2] = 1