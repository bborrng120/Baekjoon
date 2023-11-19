import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
visit = [0]*n
maxs = 0

def back(li):
    global maxs
    
    if len(li) == n:
        ans = 0
        for i in range(n-1):
            ans += abs(li[i]-li[i+1])
            maxs = max(ans,maxs)
        return
    
    for i in range(n):
        if visit[i]==0:
            visit[i] = 1
            li.append(my_list[i])
            back(li)
            visit[i] = 0
            li.pop()

back([])
print(maxs)
