import heapq
import sys

t = int(sys.stdin.readline())
q = []
for _ in range(t):
    n = int(sys.stdin.readline())
    if n == 0:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q,(abs(n),n))