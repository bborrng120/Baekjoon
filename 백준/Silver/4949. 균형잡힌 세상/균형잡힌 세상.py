import sys

while True:
    s = sys.stdin.readline().rstrip()
    q = []
    if s =='.':
        break
    for i in s:
        if i == '(' or i == '[':
            q.append(i)
        elif i == ')':
            if q and q[-1] == '(':
                q.pop()
            else:
                q.append(i)
        elif i == ']':
            if q and q[-1] == '[':
                q.pop()
            else:
                q.append(i)
        else:
            continue
        
    if not q:
        print('yes')
    else:
        print('no')