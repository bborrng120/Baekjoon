import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
my_list = list(map(int, sys.stdin.readline().split()))
my_list.sort()

for _ in range(m):
    a = heapq.heappop(my_list)
    b = heapq.heappop(my_list)
    heapq.heappush(my_list, a+b)
    heapq.heappush(my_list, a+b)
    
print(sum(my_list))