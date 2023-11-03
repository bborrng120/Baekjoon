import sys

n = int(sys.stdin.readline())
my_list = [[] for _ in range(n-1)]
d = [[0]*2 for _ in range(n)]

for i in range(n-1):
    a, b = map(int,sys.stdin.readline().split())
    my_list[i].extend([a,b])
k = int(sys.stdin.readline())

if n > 1:
    d[1][0] = my_list[0][0]
    d[1][1] = 5000
if n > 2:
    d[2][0] = min(d[1][0]+my_list[1][0],d[0][0]+my_list[0][1])
    d[2][1] = 5000
for i in range(3, n):
    d[i][0] = min(d[i-1][0]+my_list[i-1][0],d[i-2][0]+my_list[i-2][1])
    d[i][1] = min(d[i-3][0]+k,d[i-1][1]+my_list[i-1][0],d[i-2][1]+my_list[i-2][1])
    
print(min(d[n-1]))