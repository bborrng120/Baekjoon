import sys

d = [1]*251
d[2] = 3
for i in range(3,251):
    d[i] = d[i-1]+d[i-2]*2

while True:
    try:
        n = int(sys.stdin.readline())
        print(d[n])
    except:
        break