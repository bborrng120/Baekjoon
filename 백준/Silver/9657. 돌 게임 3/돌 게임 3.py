import sys

n = int(sys.stdin.readline())
d = [0,1,0,1,1]
for i in range(5,n+1):
    if d[i-1]==0 or d[i-3]==0 or d[i-4]==0:
        d.append(1)
    else:
        d.append(0)
if d[n] == 1:
    print('SK')
else:
    print('CY')