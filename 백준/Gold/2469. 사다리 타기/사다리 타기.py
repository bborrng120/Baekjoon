import sys

k = int(sys.stdin.readline())
n = int(sys.stdin.readline())
compare = list(sys.stdin.readline().strip())
my_list = [sys.stdin.readline().strip() for _ in range(n)]

top_chrs = [chr(ord('A') + i) for i in range(k)]
for i in range(n):
    if my_list[i][0] == "?":
        q_idx = i
        break
    for j in range(k-1):
        if my_list[i][j] == "-":
            top_chrs[j], top_chrs[j+1] = top_chrs[j+1], top_chrs[j]
            
bottom_chrs = compare
for i in range(n-1, q_idx, -1):
    for j in range(k-1):
        if my_list[i][j] == "-":
            bottom_chrs[j], bottom_chrs[j+1] = bottom_chrs[j+1], bottom_chrs[j]
            
ans = []
for i in range(k-1):
    if top_chrs[i] == bottom_chrs[i]:
        ans.append("*")
    elif top_chrs[i] == bottom_chrs[i+1] and top_chrs[i+1] == bottom_chrs[i]:
        ans.append("-")
        bottom_chrs[i], bottom_chrs[i+1] = bottom_chrs[i+1], bottom_chrs[i]
    else:
        ans = ["x"]*(k-1)
        break
print("".join(ans))
