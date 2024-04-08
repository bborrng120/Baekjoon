import sys

n = int(sys.stdin.readline())
egg = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
ans = 0

def breakEgg(d):
    global ans
    
    if d==n:
        count = 0
        for k in egg:
            if k[0]<=0:
                count += 1
                
        ans = max(ans,count)
        return
    
    breaks = True
    for i in range(n):
        if i!=d and egg[d][0]>0 and egg[i][0]>0:
            egg[d][0]-=egg[i][1]
            egg[i][0]-=egg[d][1]
            breakEgg(d+1)
            egg[d][0]+=egg[i][1]
            egg[i][0]+=egg[d][1]
            breaks = False
    if breaks:
        breakEgg(d+1)
            

breakEgg(0)
print(ans)