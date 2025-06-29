import sys

n, l = map(int, sys.stdin.readline().split())
my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans, cur = 0, 0

my_list.sort()

for s, e in my_list:
    if cur > s:
        s = cur
        
    while s <= e-1:
        s += l
        ans += 1
    cur = s
    
print(ans)
