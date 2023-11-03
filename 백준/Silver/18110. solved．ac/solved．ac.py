from collections import deque
import math
import sys

def rounds(n):
    if n - math.floor(n) >= 0.5:
        return int(n)+1
    else:
        return int(n)

n = int(input())
m = rounds(n*0.15)
my_list = deque()

if n == 0:
    print(0)
    exit()
    
for _ in range(n):
    my_list.append(int(sys.stdin.readline()))

my_list = deque(sorted(my_list))
    
for _ in range(m):
    my_list.popleft()
    my_list.pop()

print(rounds(sum(my_list)/len(my_list)))