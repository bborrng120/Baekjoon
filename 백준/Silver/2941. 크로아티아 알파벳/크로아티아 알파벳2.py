import sys

my = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = sys.stdin.readline().strip()
for i in my:
    s = s.replace(i,'*')
print(len(s))
