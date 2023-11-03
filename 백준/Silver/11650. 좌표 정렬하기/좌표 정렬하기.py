import sys

n = int(sys.stdin.readline())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
b = sorted(a)
for i in b:
    for j in i:
        print(j, end=" ")
    print()