import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(sys.stdin.readline().split())
my_list.sort()
my = ['a','e','i','o','u']
your = ['b','c','d','f','g','h','j','k','k','m','n','p','q','r','s','t','v','w','x','y','z']
s = []

def back(x):
    my_count, your_count = 0, 0
    if len(s) == n:
        for i in s:
            if i in my:
                my_count += 1
            else:
                your_count += 1
        
        if my_count > 0 and your_count > 1:
            print(''.join(s))
            return
        return
    
    for i in range(x,m):
        s.append(my_list[i])
        back(i+1)
        s.pop()

back(0)
