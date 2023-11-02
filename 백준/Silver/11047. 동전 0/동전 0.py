import sys

n, mon = map(int,sys.stdin.readline().split())
my_list = []
sum = 0

for _ in range(n):
    my_list.append(int(sys.stdin.readline()))
    
while mon != 0:
    max = 0
    for i in my_list:
        if mon < i:
            break
        elif max < i and mon >= i:
            max = i
    sum += mon//max
    mon %= (mon//max)*max
print(sum)