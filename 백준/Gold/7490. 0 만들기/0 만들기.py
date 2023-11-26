import sys

def back(x,d):
    global ans
    
    if x==n:
        res = ''.join([i for i in s if i != ' '])
        if eval(res)==0:
            ans = ''.join(s)
            print(ans)
        return
    
    if d%2!=0:
        s.append(str(x+1))
        back(x+1,d+1)
        s.pop()
            
    else:
        for i in range(3):
            if i==0:
                s.append(' ')
            elif i==1:
                s.append('+')
            else:
                s.append('-')
            back(x,d+1)
            s.pop()

t = int(sys.stdin.readline())
for _ in range(t):
    s = ['1']
    ans = ''
    n = int(sys.stdin.readline())
    back(1,2)
    print()