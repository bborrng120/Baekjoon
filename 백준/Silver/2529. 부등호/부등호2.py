import sys

k = int(sys.stdin.readline())
my_list = sys.stdin.readline().split()
s = []
maxs = ''
mins = ''

def checkop(x,y,o):
    if o == '<':
        return x < y
    else:
        return x > y

def back(count):
    global mins, maxs
    
    if len(s)==k+1:
        if mins == '':
            mins = ''.join(map(str, s))
        else:
            maxs = ''.join(map(str, s))
            
        return
    
    for i in range(10):
        if i in s:
            continue
        if len(s)==0 or checkop(s[-1],i,my_list[count-1]):
            s.append(i)
            back(count+1)
            s.pop()
            
        
back(0)
print(maxs)
print(mins)
