import sys

n, s, r = map(int, sys.stdin.readline().split())
lost = list(map(int, sys.stdin.readline().split()))
reserve = list(map(int, sys.stdin.readline().split()))

lost_n = set(lost) - set(reserve)
reserve_n = set(reserve) - set(lost)

for i in reserve_n:
    if i-1 in lost_n:
        lost_n.remove(i-1)
    elif i+1 in lost_n:
        lost_n.remove(i+1)
        
print(len(lost_n))