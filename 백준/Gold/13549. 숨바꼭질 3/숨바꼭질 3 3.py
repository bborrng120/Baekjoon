import sys
import heapq

n, m = map(int,sys.stdin.readline().split())
INF = int(1e9)
distance = [INF]*100001
        
def move(x):
    my_list = [(0,x*2),(1,x-1),(1,x+1)]
    return my_list
    
        
def dik(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    
    while q:
        dist, v = heapq.heappop(q)
        
        if distance[v] < dist:
            continue
        
        my_list = move(v)
        for i in my_list:
            cost = dist + i[0]
            if 0<=i[1]<=100000 and cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))
        
    
    
dik(n)
print(distance[m])
