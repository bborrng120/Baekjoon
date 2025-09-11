import sys

t = 0
while True:
    s = sys.stdin.readline().rstrip()
    stack = []
    cnt = 0
    t += 1
    
    if '-' in s:
        break
    
    for i in s:
        if i == '{':
            stack.append(i)
        else:
            if not stack:
                stack.append('{')
                cnt += 1
            else:
                stack.pop()
                    
    cnt += len(stack)//2
                
    print(f"{t}. {cnt}")