import sys

n, m= map(int, sys.stdin.readline().split())
count = 0

matrix = [[0]*(n+1) for i in range(n+1)]
v_dfs = [0]*(n+1)
check = [0]*(n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1
                
def dfs(start_node):
    stack = list()
    stack.append(start_node)
    
    while stack:
        node = stack.pop()
        if v_dfs[node] != 1:
            v_dfs[node] = 1
            check[node] = 1
            s = []
            for i in range(1, n+1):
                if matrix[node][i] == 1 and v_dfs[i] == 0:
                    s.append(i)
            stack.extend(reversed(s))

for i in range(1, len(check)):
    if check[i] != 1:
        count+=1
        dfs(i)
        
print(count)
