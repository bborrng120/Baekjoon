import sys

a,b,c = map(int,sys.stdin.readline().split())
visit = [[0]*(b+1) for _ in range(a+1)]
ans = []

def dfs(x,y):
    if 0<=x<=a and 0<=y<=b:
        if visit[x][y]==0:
            visit[x][y]=1
        else:
            return
            
    z = c-x-y
    if x==0:
        ans.append(z)
        
    water = min(x,b-y)
    dfs(x-water,y+water)
    water = min(x,c-z)
    dfs(x-water,y)
            
    water = min(y,a-x)
    dfs(x+water,y-water)
    water = min(y,c-z)
    dfs(x,y-water)
            
    water = min(z,a-x)
    dfs(x+water,y)
    water = min(z,b-y)
    dfs(x,y+water)
            
dfs(0,0)
print(*sorted(ans))
