import sys

x1, y1 = map(int,sys.stdin.readline().split())
x2, y2 = map(int,sys.stdin.readline().split())
x3, y3 = map(int,sys.stdin.readline().split())

ans = (y2-y1)*(x3-x2) - (y3-y2)*(x2-x1)

if ans>0:
    print(-1)
elif ans==0:
    print(0)
else:
    print(1)