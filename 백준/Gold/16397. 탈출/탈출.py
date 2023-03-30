import sys, math
from collections import deque
def press_btn():
    visit = [0]*100000
    visit[N] = 1
    q = deque([[N, 0]])
    while q:
        n, cnt = q.popleft()
        if n == G:
            print(cnt)
            return
        if cnt == T: continue
        if n+1 <= 99999 and not visit[n+1]:
            visit[n+1] = 1
            q.append([n+1, cnt+1])
        if 0 < n*2 <= 99999:
            new = n*2 - (10**int(math.log10(n*2)))
            if not visit[new]:
                visit[new] = 1
                q.append([new, cnt+1])
    print("ANG")

input = sys.stdin.readline
N, T, G = map(int, input().split())

press_btn()
