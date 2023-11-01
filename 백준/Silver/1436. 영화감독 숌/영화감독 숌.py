import sys

n = int(sys.stdin.readline())
num = 666
count = 0

while True:
    if '666' in str(num):
        count += 1
    if n == count:
        print(num)
        break
    num += 1