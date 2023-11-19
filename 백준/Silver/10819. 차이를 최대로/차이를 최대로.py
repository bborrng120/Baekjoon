import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
visit = [0]*n
maxs = 0
li = []

def back():
    global maxs
    
    if len(li) == n:
        ans = 0
        for i in range(n-1):
            ans += abs(li[i]-li[i+1])
        maxs = max(ans,maxs)
        return
    
    for i in range(n):
        if visit[i]==0:
            li.append(my_list[i])
            visit[i] = 1
            back()
            visit[i] = 0
            li.pop()

back()
print(maxs)