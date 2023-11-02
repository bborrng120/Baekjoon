import sys

time = []
count = 1
n = int(sys.stdin.readline())
for _ in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))

time = sorted(time, key=lambda a: a[0])
time = sorted(time, key=lambda a: a[1])

a = time[0][1]
for i in range(1, len(time)):
    if a <= time[i][0]:
        a = time[i][1]
        count += 1
print(count)