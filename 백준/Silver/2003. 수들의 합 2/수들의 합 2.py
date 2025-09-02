import sys

n, m = map(int, sys.stdin.readline().split())
my_list = list(map(int, sys.stdin.readline().split()))
s, e = 0, 0
sums, ans = 0, 0

while True:
    if sums >= m:
        sums -= my_list[s]
        s += 1
    elif e == n:
        break
    else:
        sums += my_list[e]
        e += 1
    if sums == m:
        ans += 1
        
print(ans)