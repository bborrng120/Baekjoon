import sys
sys.setrecursionlimit(10**6)

n, m= map(int, sys.stdin.readline().split())
count = 0

matrix = [[0]*(n+1) for i in range(n+1)]
v_dfs = [0]*(n+1)
check = [0]*(n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1
                
def dfs(v):
    v_dfs[v] = 1
    check[v] = 1
    for i in range(1, n+1):
        if v_dfs[i] == 0 and matrix[v][i] == 1:
            dfs(i)

for i in range(1, len(check)):
    if check[i] != 1:
        count+=1
        dfs(i)
        
print(count)
