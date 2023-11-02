import sys

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(19)]
dx = [1,0,-1,1]
dy = [0,1,1,1]

for i in range(19):
    for j in range(19):
        if graph[i][j] == 1 or graph[i][j] == 2:
            check = []
            for k in range(4):
                if 0<=i+dx[k]<19 and 0<=j+dy[k]<19 and graph[i+dx[k]][j+dy[k]] == graph[i][j]:
                    if 0<=i-dx[k]<19 and 0<=j-dy[k]<19:
                        if graph[i][j]!=graph[i-dx[k]][j-dy[k]]:
                            check.append((dx[k],dy[k]))
                    else:
                        check.append((dx[k],dy[k]))
            for a,b in check:
                x, y = i+a, j+b
                count = 1
                while 0<=x<19 and 0<=y<19 and graph[x][y]==graph[i][j]:
                    count+=1
                    x = x+a
                    y = y+b
                if count == 5:
                    print(graph[i][j])
                    print(i+1,j+1)
                    sys.exit(0)
print(0)