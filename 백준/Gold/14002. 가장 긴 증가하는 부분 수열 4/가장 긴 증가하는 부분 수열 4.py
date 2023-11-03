import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
d = [[1,i] for i in my_list]
c = []
mm, m = 1, 0

for i in range(1,n):
    for j in range(i):
        if my_list[i] > my_list[j]:
            d[i][0] = max(d[i][0],d[j][0]+1)
    if mm < d[i][0]:
        mm = d[i][0]
        m = i


for i in range(m,-1,-1):
    if d[i][0] == mm:
        c.append(d[i][1])
        mm -= 1
        
c.reverse()
print(len(c))
print(*c)