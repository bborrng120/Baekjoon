from collections import deque

n = int(input())
my_list = list(map(int,input().split()))
s = int(input())
visit = [0]*n
count = 1

def bfs(x):
    global count
    q = deque([x])
    
    while q:
        x = q.popleft()
        
        for i in range(2):
            if i==0:
                dx = x-my_list[x]
            elif i==1:
                dx = x+my_list[x]
            
            if 0<=dx<n and visit[dx]==0:
                visit[dx]=1
                count += 1
                q.append(dx)
                    
bfs(s-1)
print(count)
