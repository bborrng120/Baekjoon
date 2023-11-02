import sys

n = int(sys.stdin.readline())
graph = []
count = 0
for _ in range(n):
    a, b = map(int,sys.stdin.readline().split())
    graph.append((a,b))
    
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            a = (graph[i][0]-graph[j][0])**2 + (graph[i][1]-graph[j][1])**2
            b = (graph[j][0]-graph[k][0])**2 + (graph[j][1]-graph[k][1])**2
            c = (graph[i][0]-graph[k][0])**2 + (graph[i][1]-graph[k][1])**2
            if max(a,b,c)*2 == a+b+c:
                count+=1
print(count)