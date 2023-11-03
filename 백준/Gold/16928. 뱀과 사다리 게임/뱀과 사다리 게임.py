from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
ladder =  {}
snake = {}
visit = [0]*101


for _ in range(n):
    a, b = map(int,sys.stdin.readline().split())
    ladder[a] = b
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    snake[a] = b
    
def bfs(x):
    q = deque([(x,0)])
    visit[x] = 1
    
    while q:
        node, count = q.popleft()
        
        if node == 100:
            return count
            
        for i in range(1,7):
            nx = node + i
            if nx < 101 and visit[nx] == 0:
            	if nx in ladder:
                	q.append((ladder[nx],count+1))
                	visit[ladder[nx]] = 1
            	elif nx in snake:
                	q.append((snake[nx],count+1))
                	visit[snake[nx]] = 1
            	else:
            		q.append((nx,count+1))
            	visit[nx] = 1
print(bfs(1))