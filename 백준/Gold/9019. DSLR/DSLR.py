from collections import deque
import sys

n = int(sys.stdin.readline())

def left(x):
    x = x[1:] + x[0]
    return x

def right(x):
    x = x[-1] + x[:-1]
    return x

def double(x):
    x = str(int(x)*2)
    if int(x) > 9999:
        x = str(int(x)%10000)
    if len(x) == 1:
        x = '000' + x
    elif len(x) == 2:
        x = '00' + x
    elif len(x) == 3:
        x = '0' + x
            
    return x

def subtract(x):
    x = str(int(x)-1)
    if int(x) < 0:
        x = '9999'
    if len(x) == 1:
        x = '000' + x
    elif len(x) == 2:
        x = '00' + x
    elif len(x) == 3:
        x = '0' + x
    return x


for _ in range(n):
    d = ['']*10000
    count = 0
    a, b = sys.stdin.readline().split()
    
    if len(a) == 1:
        a = '000' + a
    elif len(a) == 2:
        a = '00' + a
    elif len(a) == 3:
        a = '0' + a
        
    if len(b) == 1:
        b = '000' + b
    elif len(b) == 2:
        b = '00' + b
    elif len(b) == 3:
        b = '0' + b
    
    
    queue = deque()
    queue.append(a)
    isSuccess = False
    while queue:
        s = queue.popleft()
    
        for i in range(4):
            if i == 0:
                f = subtract(s)
                dslr = 'S'
            elif i == 1:
                f = double(s)
                dslr = 'D'
            elif i == 2:
                f = left(s)
                dslr = 'L'
            else:
                f = right(s)
                dslr = 'R'
        
            if not d[int(f)]:
                queue.append(f)
                d[int(f)] = d[int(s)]+dslr
                if f == b:
                    print(d[int(f)])
                    isSuccess = True

        if isSuccess:
            break