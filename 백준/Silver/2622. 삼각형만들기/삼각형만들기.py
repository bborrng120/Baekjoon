import sys

n = int(sys.stdin.readline())
count = 0

for i in range(1,n):
    for j in range(i,n):
        k = n-i-j
        if k>=j and i+j>k:
            count+=1
            
print(count)