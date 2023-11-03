import sys

n, m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
l,r,lm,rm = 0,m-1,0,0
ans = 0

while l < r:
	if my_list[l] <= my_list[r]:
		if lm < my_list[l]:
			lm = my_list[l]
		else:
			ans += lm-my_list[l]
		l+=1
	else:
		if rm < my_list[r]:
			rm = my_list[r]
		else:
			ans += rm-my_list[r]
		r-=1
print(ans)