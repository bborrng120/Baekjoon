n = int(input())
k = 2*n-1
for i in range(1,n+1):
    c = 2*i-1
    print(' '*((k-c)//2)+'*'*c)