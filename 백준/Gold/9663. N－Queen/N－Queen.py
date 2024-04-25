import sys

n = int(sys.stdin.readline())
my_list = [0]*n
count = 0
visit = [False]*n

def back(x):
    global count
    
    if x==n:
        count += 1
        return
    
    for i in range(n):
    	if visit[i]==False:
    		my_list[x] = i
    		
    		if check(x):
    			visit[i] = True
    			back(x+1)
    			visit[i] = False
        
def check(x):
    for i in range(x):
        if abs(i-x)==abs(my_list[i]-my_list[x]):
            return False
    return True

back(0)
print(count)