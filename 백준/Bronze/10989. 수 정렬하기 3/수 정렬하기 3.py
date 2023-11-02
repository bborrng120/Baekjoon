import sys

n = int(sys.stdin.readline())
a = [0]*10001

for _ in range(n):
    num = int(sys.stdin.readline())
    a[num] += 1
for i in range(1,10001):
    for _ in range(a[i]):
        print(i)