import sys

n, m = map(int, sys.stdin.readline().split())
my_list = list(map(int, sys.stdin.readline().split()))
s, e = 0, 1
sums, ans = 0, 0

while e <= n:
    sums = sum(my_list[s:e])
    
    if sums < m:
        e += 1
    else:
        if sums == m:
            ans += 1
        s += 1
        
print(ans)
