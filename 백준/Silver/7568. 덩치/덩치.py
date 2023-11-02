import sys

n = int(sys.stdin.readline())
my_list = []
check = [1]*n
count = 0
for _ in range(n):
    a, b = map(int,sys.stdin.readline().split())
    my_list.append((a,b))

for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue
        elif my_list[j][0]>my_list[i][0] and my_list[j][1]>my_list[i][1]:
            count += 1
    check[i] += count
print(*check)