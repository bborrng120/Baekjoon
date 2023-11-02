import sys

n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())
    my_list = [list(map(int,sys.stdin.readline().split())) for _ in range(2)]
    d = [[0]*(m+1) for _ in range(2)]
    
    d[0][1], d[1][1] = my_list[0][0], my_list[1][0]
    
    for i in range(2,m+1):
        d[0][i] = max(d[1][i-1]+my_list[0][i-1],max(d[0][i-2],d[1][i-2])+my_list[0][i-1])
        d[1][i] = max(d[0][i-1]+my_list[1][i-1],max(d[0][i-2],d[1][i-2])+my_list[1][i-1])
        
    print(max(d[0][m],d[1][m]))
