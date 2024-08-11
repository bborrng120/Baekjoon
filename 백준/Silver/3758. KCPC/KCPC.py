import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    n, k, t, m = map(int, sys.stdin.readline().split())
    score = [[i, [0 for _ in range(k+1)], 0, 0] for i in range(n+1)]
    score[0][1][0] = -int(1e9)
    time = 0
    
    for _ in range(m):
        i, j, s = map(int, sys.stdin.readline().split())
        time += 1
        score[i][3] = time
        score[i][2] += 1
        
        if s > score[i][1][j]:
            score[i][1][j] = s
        
    score.sort(key=lambda x: (-sum(x[1]), x[2], x[3]))
    
    for p, q in enumerate(score):
        if q[0]==t:
            print(p+1)
            break