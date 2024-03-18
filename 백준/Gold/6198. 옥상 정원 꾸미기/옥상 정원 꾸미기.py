import sys

n = int(sys.stdin.readline())
building = []
s = []
ans = 0

for i in range(n):
    building.append(int(sys.stdin.readline()))
    
for i in range(n):
	while s and s[-1]<=building[i]:
		s.pop()
		
	s.append(building[i])
	ans += len(s)-1
	
print(ans)