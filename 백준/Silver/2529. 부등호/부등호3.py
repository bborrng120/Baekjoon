import sys

k = int(sys.stdin.readline())
my_list = sys.stdin.readline().split()
s = []
maxs = 0
mins = int(1e11)
maxss = ''
minss = ''

def checkop(x,y,o):
    if o == '<':
        return x < y
    else:
        return x > y

def back(count):
    global mins, maxs, maxss, minss
    
    if len(s)==k+1:
        if maxs < int(''.join(map(str, s))):
            maxs = int(''.join(map(str, s)))
            maxss = ''.join(map(str, s))
        if mins > int(''.join(map(str, s))):
            mins = int(''.join(map(str, s)))
            minss = ''.join(map(str, s))
            
        return
    
    for i in range(10):
        if i in s:
            continue
        if len(s)==0 or checkop(s[-1],i,my_list[count-1]):
            s.append(i)
            back(count+1)
            s.pop()
            
        
back(0)
print(maxss)
print(minss)
