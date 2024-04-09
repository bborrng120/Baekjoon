import sys

n = int(sys.stdin.readline())
nums = [str(i) for i in range(10)]
res = []
l = []

def back():
    if len(l)>0:
        res.append(int(''.join(l)))
    
    for i in nums:
        if len(l)==0 or int(l[-1])>int(i):
            l.append(i)
            back()
            l.pop()
            
back()
res.sort()

if len(res)>=n:
    print(res[n-1])
else:
    print(-1)
