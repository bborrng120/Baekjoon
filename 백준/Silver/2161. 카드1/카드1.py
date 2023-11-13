from collections import deque
import sys

n = int(sys.stdin.readline())
q = deque([i for i in range(1,n+1)])
ans = []
while len(q) > 1:
    ans.append(q.popleft())
    q.append(q.popleft())
ans.append(q.popleft())
print(*ans)