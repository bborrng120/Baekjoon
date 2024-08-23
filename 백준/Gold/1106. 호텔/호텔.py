import sys

c, n = map(int, sys.stdin.readline().split())
my_list = [(0,0)]
d = [0]*100001
check = False

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    my_list.append((a,b))

for i in range(1, n+1):
    for j in range(my_list[i][0], 100001):
        d[j] = max(d[j], d[j-my_list[i][0]] + my_list[i][1])
        
for i in range(1, 100001):
    if d[i]>=c:
        print(i)
        break