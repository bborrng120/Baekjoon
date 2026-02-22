import sys

n, m, r = map(int, sys.stdin.readline().split())
my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def rotate(k):
    if k > n-k-1:
        return
    if k > m-k-1:
        return
    
    temp = my_list[k][k]
    
    for i in range(k, m-k-1):
        my_list[k][i] = my_list[k][i+1]
    for i in range(k, n-k-1):
        my_list[i][m-k-1] = my_list[i+1][m-k-1]
    for i in range(m-k-1, k, -1):
        my_list[n-k-1][i] = my_list[n-k-1][i-1]
    for i in range(n-k-1, k, -1):
        my_list[i][k] = my_list[i-1][k]
        
    my_list[k+1][k] = temp

for i in range(min(n, m)//2):
    c_len = (m-2*i) * 2 + ((n-2*i)-2) * 2
    for _ in range(r % c_len):
        rotate(i)
        
for i in my_list:
    print(*i)
