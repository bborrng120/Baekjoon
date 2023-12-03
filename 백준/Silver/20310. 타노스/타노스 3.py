from collections import deque
import sys

s = sys.stdin.readline().strip()
o_list,z_list = deque([]),deque([])

for i in range(len(s)):
    if s[i]=='0':
        z_list.append((i,'0'))
    else:
        o_list.append((i,'1'))
        
for _ in range(len(z_list)//2):
    z_list.pop()
    
for _ in range(len(o_list)//2):
    o_list.popleft()
    
ans_list = sorted(z_list+o_list)

for i in ans_list:
    print(i[1], end='')
