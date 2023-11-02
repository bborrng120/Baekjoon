n, m = map(int, input().split())
seta = set()
setb = set()
for _ in range(n):
    seta.add(input())
for _ in range(m):
    setb.add(input())
print(len(seta&setb))
for i in sorted(seta&setb):
    print(i)
