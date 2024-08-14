import sys

n, m = map(int, sys.stdin.readline().split())
d = [i for i in range(m+1)]
my_list = []

for _ in range(n):
    s, e, c = map(int, sys.stdin.readline().split())
    my_list.append((s,e,c))
    
my_list.sort()

for i in range(n):
    s, e, c = my_list[i]
    if 0<=s<=m and 0<=e<=m:
        if c < d[e]-d[s]:
            d[e] = c + d[s]
            for i in range(e+1, m+1):
                d[i] = min(d[i], d[e]+(i-e))
print(d[m])