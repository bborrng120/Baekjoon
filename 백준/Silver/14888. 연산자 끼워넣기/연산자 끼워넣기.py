from itertools import permutations
import sys

n = int(sys.stdin.readline())
cal = list(map(int,sys.stdin.readline().split()))
a = []
mins, maxs = int(1e10), -int(1e10)
my_list = list(map(int,sys.stdin.readline().split()))

for i in range(4):
    for _ in range(my_list[i]):
        if i == 0:
            a.append('+')
        elif i == 1:
            a.append('-')
        elif i == 2:
            a.append('*')
        else:
            a.append('//')
            
all = list(permutations(a,n-1))

for i in list(set(all)):
	ans = cal[0]
	for j in range(n-1):
		if i[j] == '+':
			ans += cal[j+1]
		elif i[j] == '-':
			ans -= cal[j+1]
		elif i[j] == '*':
			ans *= cal[j+1]
		else:
			if ans < 0:
				ans = abs(ans)//cal[j+1]
				ans = -ans
			else:
				ans //= cal[j+1]
	maxs = max(ans,maxs)
	mins = min(ans,mins)
	
print(maxs)
print(mins)