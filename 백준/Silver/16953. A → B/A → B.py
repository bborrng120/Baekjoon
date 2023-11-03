from collections import deque
import sys
 
def bfs(l):
    num = int(l)
    q = deque([(num,0)])
 
    while q:
        num,count = q.popleft()
        if num == int(m):
            return count
        for i in range(2):
            if i==0:
                if num*2 <= int(m):
                    q.append((num*2,count+1))
            else:
                if int(str(num)+'1') <= int(m):
                    q.append((int(str(num)+'1'),count+1))
    return
 
 
s = sys.stdin.readline().strip()
n, m = s.split()
check = bfs(int(n))
if check:
    print(check+1)
else:
    print(-1)