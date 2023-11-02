import sys

n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
count = 0

for i in my_list:
    if i > 1:
        for j in range(2,i):
            if i% j == 0:
                count -= 1
                break
        count += 1
print(count)