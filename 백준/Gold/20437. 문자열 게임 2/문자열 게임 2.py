from collections import defaultdict
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    mins,maxs = int(1e9),0
    check = False
    
    my_dict = defaultdict(list)
    for i in range(len(s)):
        my_dict[s[i]].append(i)
        
    for i in my_dict.values():
        if len(i) >= n:
            check = True
            for j in range(len(i)-n+1):
                sub = i[j:j+n]
                mins = min(mins,sub[-1]-sub[0]+1)
                maxs = max(maxs,sub[-1]-sub[0]+1)
    
    
    if check:
        print(mins,maxs)
    else:
        print(-1)