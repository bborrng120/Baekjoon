import sys

game, win = map(int,sys.stdin.readline().split())
comp = int(win*100/game)
res = -1
l, r = 1, 1000000000

while l<=r and comp != 100:
    mid = (l+r)//2
    a, b = game+mid, win+mid
    ans = int(b*100/a)
    
    if ans > comp:
        r = mid-1
        res = mid
    elif ans == comp:
        l = mid+1
print(res)