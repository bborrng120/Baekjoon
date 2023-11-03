from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
q = deque()

for i in range(1,n+1):
    q.append(i)
    
print('<',end="")
while len(q) != 1:
    for _ in range(m-1):
        q.append(q.popleft())
    ans = q.popleft()
    print(f'{ans}, ',end="")
print(f'{q[0]}>')