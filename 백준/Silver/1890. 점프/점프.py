import sys

n = int(sys.stdin.readline())
game = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]
d[0][0] = 1

for i in range(n):
    for j in range(n):
        if d[i][j] != 0:
        	if i == n-1 and j == n-1:
        		continue
        	for k in range(2):
        		if k == 0:
        			a = i
        			b = j + game[i][j]
        		else:
        			a = i + game[i][j]
        			b = j
        		if 0<=a<n and 0<=b<n:
        			d[a][b] += d[i][j]
print(d[n-1][n-1])