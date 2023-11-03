import sys
 
def dfs(depth, idx):
    global min_diff
    if depth == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(i + 1, n):
                if visited[i] and visited[j]:
                    power1 += (graph[i][j]+graph[j][i])
                elif not visited[i] and not visited[j]:
                    power2 += (graph[i][j]+graph[j][i])
        min_diff = min(min_diff, abs(power1-power2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


n = int(sys.stdin.readline())

visited = [False for _ in range(n)]
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
min_diff = int(1e9)

dfs(0, 0)
print(min_diff)