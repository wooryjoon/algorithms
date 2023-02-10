from collections import deque
from itertools import permutations

ans = 10**9
dx, dy, dz = (1, -1, 0, 0, 0, 0), (0, 0, 1, -1, 0, 0), (0, 0, 0, 0, 1, -1)
a = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
b = [[[0]*5 for _ in range(5)] for _ in range(5)]

def bfs():
    global ans
    q = deque()
    q.append((0, 0, 0))
    dist = [[[-1]*5 for _ in range(5)] for _ in range(5)]
    dist[0][0][0] = 0
    while q:
        x, y, z = q.popleft()
        if (x, y, z) == (4, 4 ,4):
            ans = min(ans ,dist[x][y][z])
            if ans == 12:
                print(12)
                exit(0)
            return
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or nz < 0 or nz >= 5:
                continue
            if b[nx][ny][nz] and dist[nx][ny][nz] == -1:
                q.append((nx, ny, nz))
                dist[nx][ny][nz] = dist[x][y][z]+1

def rotate(k):
    temp = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp[j][4-i] = b[k][i][j]
    b[k] = temp

def maze(cnt):
    if cnt == 5:
        if b[4][4][4]:
            bfs()
        return
    for i in range(4):
        if b[0][0][0]:
            maze(cnt+1)
        rotate(cnt)

def solve():
    for d in permutations([0, 1, 2, 3, 4]):
        for i in range(5):
            b[d[i]] = a[i]
        maze(0)

solve()
print(ans if ans != 10**9 else -1)
