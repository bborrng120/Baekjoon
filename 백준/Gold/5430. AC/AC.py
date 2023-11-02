from collections import deque
import sys

t = int(sys.stdin.readline())

def rd(x,l):
    global boo
    
    for j in x:
        if j == 'R':
            boo = not boo
        elif j == 'D':
            if len(l) < 1:
                return
            else:
                if boo:
                    l.pop()
                else:
                    l.popleft()
    return l

for _ in range(t):
    s = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().rstrip()
    k = ''
    boo = False
    my_list = deque()
    for i in range(len(a)):
        if a[i].isdigit():
            k += a[i]
            if a[i+1].isdigit():
                continue
            my_list.append(int(k))
            k = ''
    ab = rd(s,my_list)
    if ab == None:
        print('error')
    else:
        if boo:
            ab.reverse()
        output = '[' + ','.join(str(y) for y in ab) + ']'
        print(output)