import sys

n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
ans = 0
tx = [[0,0,1,1],[0,1,1,2],[0,0,-1,-1],[0,1,0,-1],[0,0,1,1],[0,0,0,0],[0,1,2,3],[0,1,0,0],[0,1,2,2],[0,0,0,-1],[0,0,1,2],[0,0,1,0],[0,1,1,2],[0,0,-1,0],[0,0,-1,1],[0,0,-1,-2],[0,0,0,1],[0,0,1,2],[0,1,1,1]]
ty = [[0,1,0,1],[0,0,1,1],[0,1,1,2],[0,0,1,1],[0,1,1,2],[0,1,2,3],[0,0,0,0],[0,0,1,2],[0,0,0,1],[0,1,2,2],[0,1,1,1],[0,1,1,2],[0,0,1,0],[0,1,1,2],[0,1,1,1],[0,1,1,1],[0,1,2,2],[0,1,0,0],[0,0,1,2]]

for i,j in zip(tx,ty):
    for x in range(n):
        for y in range(m):
            res = 0
            for k in range(4):
                nx = x + i[k]
                ny = y + j[k]
                if 0<=nx<n and 0<=ny<m:
                    res += graph[nx][ny]
                else:
                    res = 0
                    break
            ans = max(res,ans)
print(ans)