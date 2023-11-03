import sys

n = int(sys.stdin.readline())
d = [[0,0,0,0] for _ in range(10001)]
d[1][1], d[2][1], d[2][2], d[3][1], d[3][2], d[3][3] = 1, 1, 1, 1, 1, 1
for i in range(4,10001):
    d[i][1] = d[i-1][1]
    d[i][2] = d[i-2][1]+d[i-2][2]
    d[i][3] = d[i-3][1]+d[i-3][2]+d[i-3][3]
for _ in range(n):
    num = int(sys.stdin.readline())
    print(sum(d[num]))