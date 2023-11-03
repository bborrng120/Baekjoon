import sys

n = int(sys.stdin.readline())
m = int(input())
INF = int(1e9)
distance = [[INF]*n for _ in range(n)]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    distance[a-1][b-1] = min(distance[a-1][b-1],c)
    
for k in range(n):
    distance[k][k] = 0
    for i in range(n):
        for j in range(n):
            if distance[i][j] > distance[i][k]+distance[k][j]:
                distance[i][j] = distance[i][k]+distance[k][j]
                
for i in range(n):
    for j in range(n):
        if distance[i][j] == INF:
            print(0,end=" ")
        else:
            print(distance[i][j],end=" ")
    print()