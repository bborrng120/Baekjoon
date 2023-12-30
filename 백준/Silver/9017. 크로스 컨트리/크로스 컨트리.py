from collections import Counter
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    my_list = list(map(int,sys.stdin.readline().split()))
    c = Counter(my_list)
    
    m = max(my_list)
    ans = []
    for i in range(m+1):
        ans.append([0,0,i,0])
    k = 1
    for i in range(n):
        if c[my_list[i]]>=6:
            if ans[my_list[i]][3]<4:
                ans[my_list[i]][0] += k
            elif ans[my_list[i]][3]==4:
                ans[my_list[i]][1] = k
            ans[my_list[i]][3] += 1
            k+=1
            
    ans.sort()
    for i in range(m+1):
        if ans[i][0]!=0:
            print(ans[i][2])
            break