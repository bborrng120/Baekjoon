n = int(input())
my_list = list(map(int, input().split()))
d = [1]*n

for i in range(1, n):
    for j in range(i):
        if my_list[i] > my_list[j]:
            d[i] = max(d[i], d[j]+1)
            
print(max(d))