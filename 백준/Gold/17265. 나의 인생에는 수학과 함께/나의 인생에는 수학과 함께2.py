import sys

n = int(sys.stdin.readline())
cal = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]
max_d = [[0]*n for _ in range(n)]
min_d = [[int(1e9)]*n for _ in range(n)]
max_d[0][0], min_d[0][0] = cal[0][0], cal[0][0]

for i in range(2,n,2):
    max_d[0][i] = str(eval(max_d[0][i-2]+cal[0][i-1]+cal[0][i]))
    min_d[0][i] = str(eval(min_d[0][i-2]+cal[0][i-1]+cal[0][i]))
    max_d[i][0] = str(eval(max_d[i-2][0]+cal[i-1][0]+cal[i][0]))
    min_d[i][0] = str(eval(min_d[i-2][0]+cal[i-1][0]+cal[i][0]))
    
for i in range(1,n):
    for j in range(1,n):
        if (i+j)%2 != 0:
            continue
            
        max_d[i][j] = max(eval(max_d[i-1][j-1]+cal[i][j-1]+cal[i][j]),eval(max_d[i-1][j-1]+cal[i-1][j]+cal[i][j]))
        min_d[i][j] = min(eval(min_d[i-1][j-1]+cal[i][j-1]+cal[i][j]),eval(min_d[i-1][j-1]+cal[i-1][j]+cal[i][j]))
        if i-2>=0:
            max_d[i][j] = max(max_d[i][j],eval(max_d[i-2][j]+cal[i-1][j]+cal[i][j]))
            min_d[i][j] = min(min_d[i][j],eval(min_d[i-2][j]+cal[i-1][j]+cal[i][j]))
        if j-2>=0:
            max_d[i][j] = max(max_d[i][j],eval(max_d[i][j-2]+cal[i][j-1]+cal[i][j]))
            min_d[i][j] = min(min_d[i][j],eval(min_d[i][j-2]+cal[i][j-1]+cal[i][j]))
        
        max_d[i][j] = str(max_d[i][j])
        min_d[i][j] = str(min_d[i][j])
        
print(max_d[n-1][n-1],end=" ")
print(min_d[n-1][n-1])
