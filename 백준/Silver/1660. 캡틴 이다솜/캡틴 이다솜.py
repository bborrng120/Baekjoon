import sys

n = int(sys.stdin.readline())
ball = [1]
c, k, l = 3, 1, 2
while k < n:
    ball.append(k+c)
    k = ball[-1]
    l+=1
    c+=l
    
d = [0]*(n+1)
for i in range(1,n+1):
    d[i] = i
    
for i in ball[1:]:
    for j in range(i,n+1):
        d[j] = min(d[j],d[j-i]+1)
print(d[n])