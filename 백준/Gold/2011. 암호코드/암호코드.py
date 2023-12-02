import sys

s = sys.stdin.readline().strip()
d = [0]*(len(s)+1)

if 1<=int(s[-1])<10:
    d[1] = 1
if len(s)>1:
    if int(s[-2])!=0:
        if 10<=int(s[-2:])<27:
            d[2] = d[1]+1
        else:
            d[2] = d[1]
    
for i in range(3,len(s)+1):
    if int(s[-i])!=0:
        if 10<=int(s[-i:-i+2])<27:
            d[i] = (d[i-1]+d[i-2])
        else:
            d[i] = d[i-1]
        
print(d[-1]%1000000)