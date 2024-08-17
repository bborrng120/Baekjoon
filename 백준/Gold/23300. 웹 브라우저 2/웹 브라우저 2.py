from collections import deque
import sys

back = deque([])
front = deque([])
now = 0

n, q = map(int,sys.stdin.readline().split())
for _ in range(q):
    c = sys.stdin.readline().strip()
    if len(c)>=2:
        x, s = c.split()
        front.clear()
        if now != 0:
            back.append(now)
        now = int(s)
        
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
                for i in back:
                    if temp != i:
                        temp_list.append(i)
                        temp = i
                back = temp_list

print(now)
print(*reversed(back)) if back else print(-1)
print(*front) if front else print(-1)

