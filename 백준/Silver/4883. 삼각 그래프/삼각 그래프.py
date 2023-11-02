import sys

count = 0
while True:
    n = int(sys.stdin.readline())
    count += 1
    if n == 0:
        break
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    d = [[0]*3 for _ in range(n)]
    d[0][0],d[0][1],d[0][2] = graph[0][0],graph[0][1],graph[0][1]+graph[0][2]
    d[1][0] = d[0][1]+graph[1][0]
    d[1][1] = min(d[0][1],d[1][0],d[0][2])+graph[1][1]
    d[1][2] = min(d[0][2],d[0][1],d[1][1])+graph[1][2]
    for i in range(2,n):
        for j in range(3):
            if j==0:
                d[i][j] = min(d[i-1][1],d[i-1][0])+graph[i][0]
            elif j==1:
                d[i][j] = min(d[i-1][2],d[i-1][1],d[i-1][0],d[i][0])+graph[i][1]
            else:
                d[i][j] = min(d[i-1][2],d[i-1][1],d[i][1])+graph[i][2]
    print(f'{count}. {d[n-1][1]}')