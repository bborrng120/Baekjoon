from collections import deque
import sys
 
n, k = map(int,sys.stdin.readline().split())
my_list = list(float(sys.stdin.readline()) for _ in range(n))
my_list.sort()
 
def julsa(l):
    q = deque(l)
    for _ in range(k):
        q.pop()
        q.popleft()
    return q
 
def bojong(l):
    q = deque(l)
    for _ in range(k):
        q.pop()
        q.popleft()
    first = q[0]
    last = q[-1]
    for _ in range(k):
        q.appendleft(first)
        q.append(last)
    return q
 
j = list(julsa(my_list))
b = list(bojong(my_list))
 
print('{:.2f}'.format(sum(j)/(n-(2*k))+ 1e-8))
print('{:.2f}'.format(sum(b)/n + 1e-8))
