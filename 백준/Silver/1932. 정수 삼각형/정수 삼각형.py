import sys

n = int(sys.stdin.readline())
d = [[0] for _ in range(n+1)]
my_list = []
maxs = 0

for _ in range(n):
    my_list.append(list(map(int,sys.stdin.readline().split())))
    
for i in range(1,len(my_list)+1):
    l = len(my_list[i-1])
    for j in range(l):
        if j == 0:
            d[i][j] = d[i-1][0]+ my_list[i-1][0]
        elif j == l-1:
            d[i].append(d[i-1][j-1]+my_list[i-1][i-1])
        else:
            m = max(d[i-1][j-1]+my_list[i-1][j], d[i-1][j]+my_list[i-1][j])
            d[i].append(m)
            
for i in d:
    if max(i) > maxs:
        maxs = max(i)

print(maxs)