import sys

n = int(sys.stdin.readline())
my_list = list(map(int, sys.stdin.readline().split()))
s, e = 0, n-1
ans = 0

my_list.sort()

while s < e:
    if my_list[s] > 0:
        my_list[s] -= 1
        e -= 1
        ans += 1
    else:
        s += 1
        
print(ans)
