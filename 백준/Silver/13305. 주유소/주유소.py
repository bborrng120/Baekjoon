import sys

n = int(sys.stdin.readline())
dist = list(map(int,sys.stdin.readline().split()))
city = list(map(int,sys.stdin.readline().split()))

ans = 0
mins = int(1e10)

for i in range(n-1):
    if city[i] < mins:
        mins = city[i]
    ans += mins*dist[i]
    
print(ans)