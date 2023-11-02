import sys

n = int(sys.stdin.readline()) 
s = list(sys.stdin.readline().strip()) 
count = 0 
for i in range(n-1): 
	my_list = list(sys.stdin.readline().strip()) 
	ans = 0 
	temp = s.copy()
	for i in my_list: 
		if i in temp: 
			temp.remove(i) 
		else: 
			ans += 1 
	if ans < 2 and len(temp) < 2: 
		count += 1
print(count)