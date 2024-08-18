from collections import deque
import sys

back = deque([])
front = deque([])
now = 0
cache = 0

n, q, ct = map(int,sys.stdin.readline().split())
cache_list = list(map(int, sys.stdin.readline().split()))

for _ in range(q):
    c = sys.stdin.readline().strip()
    
    if len(c)>=2:
        x, s = c.split()
        cache += cache_list[int(s)-1]
        
        sub_temp1 = 0
        for i in front:
            sub_temp1 += cache_list[i-1]
        front.clear()
        cache -= sub_temp1
        
        if now != 0:
            back.append(now)
        now = int(s)
        
        while cache > ct:
            cache -= cache_list[back.popleft()-1]
        
    else:
        if c=='B':
            if back:
                front.appendleft(now)
                now = back.pop()
        elif c=='F':
            if front:
                back.append(now)
                now = front.popleft()
        else:
            if back:
                temp = 0
                temp_list = deque([])
                sub_temp2 = 0
                for i in back:
                    if temp != i:
                        temp_list.append(i)
                        temp = i
                    else:
                        sub_temp2 += cache_list[temp-1]
                back = temp_list
                cache -= sub_temp2

print(now)
print(*reversed(back)) if back else print(-1)
print(*front) if front else print(-1)

