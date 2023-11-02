import sys

n, k = map(int,sys.stdin.readline().split())
my_list = list(float(sys.stdin.readline()) for _ in range(n))
my_list.sort()

julsa = sum(my_list[k:n-k])/(n-(2*k))
bojong = (sum(my_list[k:n-k]) + my_list[k]*k + my_list[n-k-1]*k)/n

print('{:.2f}'.format(julsa+ 1e-8))
print('{:.2f}'.format(bojong + 1e-8))