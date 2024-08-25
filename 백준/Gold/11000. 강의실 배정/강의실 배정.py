import heapq
import sys

n = int(sys.stdin.readline())
my_list, heap = [], []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    my_list.append((a,b))
    
my_list.sort()
heap = [my_list[0][1]]
    
for i in range(1, n):
    if heap[0] <= my_list[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, my_list[i][1])
    
print(len(heap))