from collections import deque
import sys

my_list = deque(list(map(int,sys.stdin.readline().split())))

def find_num(my_list):
    my_num = int(1e9)
    for _ in range(4):
        my_list.rotate(-1)
        my_num = min(my_num,int("".join(map(str,list(my_list)))))
    return my_num

num = 1111
count = 0
my_num = find_num(my_list)

while num <= my_num:
    my = [int(x) for x in str(num)]
    if num == find_num(deque(my)):
        count += 1
    num += 1
print(count)