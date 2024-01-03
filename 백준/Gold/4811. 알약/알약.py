import sys

d = [[0]*31 for _ in range(31)]
d[1][0] = 1
for i in range(31):
    d[0][i] = 1

for i in range(1,31):
    for j in range(30):
        if j==0:
            d[i][j] = d[i-1][j+1]
        else:
            d[i][j] = d[i-1][j+1]+d[i][j-1]

while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    print(d[n][0])