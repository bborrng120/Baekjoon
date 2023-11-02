from collections import deque
import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
mins = int(1e9)

while True:
    a, b = map(int,sys.stdin.readline().split())
    if a==-1 and b==-1:
        break
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(x):
    q = deque([(x,0)])
    visit = [0]*(n+1)
    visit[x] = 1
    ans = 0
    
    while q:
        node, count = q.popleft()
        ans = max(ans,count)
        
        for i in graph[node]:
            if visit[i] == 0:
                visit[i] = 1
                q.append((i,count+1))
                
    return x, ans

for i in range(1,n+1):
    pres, score = bfs(i)
    if score < mins:
        my_list = []
        my_list.append(pres)
        mins = score
    elif score == mins:
        my_list.append(pres)

print(mins,len(my_list))
print(*my_list)