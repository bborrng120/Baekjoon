import sys

n, m = map(int,sys.stdin.readline().split())
chess = [list(sys.stdin.readline()) for _ in range(n)]
res = int(1e9)

for a in range(n-7):
    for b in range(m-7):
        bcount, wcount, ans = 0, 0, 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
                    if chess[i][j] == 'W':
                        bcount += 1
                else:
                    if chess[i][j] == 'B':
                        bcount += 1
                
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
                    if chess[i][j] == 'B':
                        wcount += 1
                else:
                    if chess[i][j] == 'W':
                        wcount += 1
        ans = min(bcount,wcount)
        res = min(res,ans)
        
print(res)