import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
count = 0
ans = []

def back(x):
	global count
	if sum(ans) == m and len(ans)>0:
		count+=1
	for i in range(x,n):
		ans.append(my_list[i])
		back(i+1)
		ans.pop()
back(0)
print(count)