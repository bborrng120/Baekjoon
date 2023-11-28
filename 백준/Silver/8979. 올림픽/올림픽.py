import sys

n, k = map(int,sys.stdin.readline().split())
country = []
ans = []

for _ in range(n):
    country.append(list(map(int,sys.stdin.readline().split())))
    
sort_country = sorted(country,key=lambda x:(-x[1],-x[2],-x[3]))

for i in country:
	a = i.pop(0)
	ans.append((a,sort_country.index(i)+1))
	
for i in ans:
	if i[0]==k:
		print(i[1])
		break