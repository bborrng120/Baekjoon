import sys

n, m = map(int,sys.stdin.readline().split())
num, div = 1, 1

for i in range(n,n-m,-1):
    num *= i
for i in range(m,0,-1):
    div *= i
print(num//div)