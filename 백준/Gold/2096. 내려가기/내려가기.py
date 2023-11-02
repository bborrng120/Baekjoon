import sys

n = int(sys.stdin.readline())
dmax=list(map(int,sys.stdin.readline().split()))
dmin=dmax.copy()
for _ in range(n-1):
	a, b, c = map(int,sys.stdin.readline().split())
	dmax = [max(dmax[0],dmax[1])+a,max(dmax[0],dmax[1],dmax[2])+b,max(dmax[1],dmax[2])+c]
	dmin = [min(dmin[0],dmin[1])+a,min(dmin[0],dmin[1],dmin[2])+b,min(dmin[1],dmin[2])+c]
print(max(dmax),end=" ")
print(min(dmin))