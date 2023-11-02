import sys

my = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = sys.stdin.readline().strip()
count = 0
st = ''
for i in range(len(s)-1):
    if s[i]+s[i+1] in my:
        if s[i-1]+s[i]+s[i+1] == 'dz=':
            count += 1
            st+=s[i-1]+s[i]+s[i+1]
        else:
            count += 1
            st+=s[i]+s[i+1]
print(count+len(s)-len(st))