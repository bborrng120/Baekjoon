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
                stack.append(i)
            else:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(i)
                    
    for i in range(len(stack)):
        if i%2 == 0:
            if stack[i] == '}':
                cnt += 1
                stack[i] = '{'
        else:
            if stack[i] == '{':
                cnt += 1
                stack[i] = '}'
                
    print(f"{t}. {cnt}")
