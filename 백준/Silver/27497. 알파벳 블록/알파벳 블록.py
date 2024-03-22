from collections import deque
import sys

q = deque([])
s = []
n = int(sys.stdin.readline())
for _ in range(n):
    button = sys.stdin.readline().split()
    
    if button[0]=='1':
        q.append(button[1])
        s.append((button[1],'1'))
    elif button[0]=='2':
        q.appendleft(button[1])
        s.append((button[1],'2'))
    else:
        if s:
            if s[-1][1]=='2':
                q.popleft()
                s.pop()
            elif s[-1][1]=='1':
                q.pop()
                s.pop()
                
if q:
	print(''.join(q))
else:
	print(0)