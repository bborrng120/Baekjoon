from itertools import combinations
import sys

n = int(sys.stdin.readline())

def check(x):
    count = 0
    if x[0][0] != x[1][0]:
        count += 1
    if x[0][1] != x[1][1]:
        count += 1
    if x[0][2] != x[1][2]:
        count += 1
    if x[0][3] != x[1][3]:
        count += 1
    return count
    
for _ in range(n):
    a = int(sys.stdin.readline())
    m = sys.stdin.readline().split()
    mins = 1000000
    
    if a > 32:
        print(0)
        continue
    
    else:
        for i in list(combinations(m,3)):
            sum, count = 0, 0
            for j in list(combinations(i,2)):
                count = check(j)
                sum += count
            if mins > sum:
                mins = sum
        print(mins)