from collections import deque
import sys
 
n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
s = int(sys.stdin.readline())
graph = [i for i in range(n)]
visit = [0]*n
count = 1
 
def bfs(x):
	global count
	
	q = deque([x])
	
	while q:
		x = q.popleft()
		
		for _ in range(2):
			x1 = x-my_list[x]
			x2 = x+my_list[x]
			
			if 0<=x1<n:
				if visit[x1]==0:
					visit[x1]=1
					count += 1
					q.append(x1)
					
			if 0<=x2<n:
				if visit[x2]==0:
					visit[x2]=1
					count += 1
					q.append(x2)
 
bfs(s-1)
print(count)