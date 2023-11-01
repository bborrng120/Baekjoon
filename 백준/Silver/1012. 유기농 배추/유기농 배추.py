import sys

def dfs(x, y):
    rcount = 0
    stack = [(x, y)]
    
    while stack:
        x, y = stack.pop()
        
        if c_matrix[y][x] == 0 and matrix[y][x] == 1:
            c_matrix[y][x] = 1
            rcount += 1

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if c_matrix[ny][nx] == 0 and matrix[ny][nx] == 1:
                    c_matrix[ny][nx] = 1
                    rcount += 1
                    stack.append((nx, ny))
                    
    return rcount
            
j = int(sys.stdin.readline())
for _ in range(j):
    count = 0
    n, m, a = map(int, sys.stdin.readline().split())
    matrix = [[0]*(n) for i in range(m)]
    c_matrix = [[0]*(n) for i in range(m)]

    for _ in range(a):
        b, c =  map(int, sys.stdin.readline().split())
        matrix[c][b] = 1

    for e in range(n):
        for f in range(m):
            if matrix[f][e] == 1:
                if dfs(e,f) != 0:
                    count += 1
    
    print(count)