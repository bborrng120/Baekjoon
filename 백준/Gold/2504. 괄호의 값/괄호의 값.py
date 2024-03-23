import sys

c = sys.stdin.readline()
s = []
ans, temp = 0, 1
pre = ''
for i in c:
	if i=='(' or i=='[':
		s.append(i)
		if i=='(':
			temp *= 2
		else:
			temp *= 3
	elif i==')' or i==']':
		if i==')':
			if not s or s[-1]=='[':
				ans = 0
				break
			if s and s[-1]=='(':
				if pre=='(' or pre=='[':
					ans += temp
				temp //= 2
				s.pop()
		else:
			if not s or s[-1]=='(':
				ans = 0
				break
			if s and s[-1]=='[':
				if pre=='(' or pre=='[':
					ans += temp
				temp //= 3
				s.pop()
	pre=i
if s:
	print(0)
else:
	print(ans)