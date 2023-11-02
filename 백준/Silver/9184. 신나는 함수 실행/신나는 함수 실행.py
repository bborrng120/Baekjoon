import sys
sys.setrecursionlimit(1000000)

d = [[[0]*101 for _ in range(101)] for _ in range(101)]
                
def w(a,b,c):
    if d[a+50][b+50][c+50]!=0:
        return d[a+50][b+50][c+50]
    
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        d[a+50][b+50][c+50] = w(20,20,20)
        return d[a+50][b+50][c+50]
    if a<b and b<c:
        d[a+50][b+50][c+50] = w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
        return d[a+50][b+50][c+50]
    else:
        d[a+50][b+50][c+50] = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        return d[a+50][b+50][c+50]
                
while True:
    a, b, c = map(int,sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1:
        break
    ans = w(a,b,c)
    print(f'w({a}, {b}, {c}) = {ans}')