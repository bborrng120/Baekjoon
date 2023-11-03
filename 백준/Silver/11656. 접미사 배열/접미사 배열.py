import sys

s = sys.stdin.readline().strip()
my_list = []
for i in range(len(s)):
    my_list.append(s[i:])
for i in sorted(my_list):
    print(i)