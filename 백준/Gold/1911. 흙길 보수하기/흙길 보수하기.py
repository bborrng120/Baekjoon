import math
import sys

n, l = map(int, sys.stdin.readline().split())
my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans, cur = 0, 0

my_list.sort()

for s, e in my_list:
    if cur > s:
        s = cur
        
    cnt = math.ceil((e-s)/l)
    ans += cnt
    
    cur = s + cnt * l
    
print(ans)