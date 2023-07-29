import sys
input = sys.stdin.readline
def dfs(p, x, y):
    global result
    if x == N-1 and y == N-1:
        result += 1
        return
    else:
        if p == 1:
            if x <= N-1 and y+1 <= N-1 and H[x][y+1] == 0:
                dfs(1, x, y+1)
            if x+1 <= N-1 and y+1 <= N-1 and H[x+1][y] == 0 and H[x][y+1] == 0 and H[x+1][y+1] == 0:
                dfs(3, x+1, y+1)
        elif p == 2:
            if x+1 <= N-1 and y <= N-1 and H[x+1][y] == 0:
                dfs(2, x+1, y)
            if x+1 <= N-1 and y+1 <= N-1 and H[x+1][y] == 0 and H[x][y+1] == 0 and H[x+1][y+1] == 0:
                dfs(3, x+1, y+1)
        elif p == 3:
            if x <= N-1 and y+1 <= N-1 and H[x][y+1] == 0:
                dfs(1, x, y+1)
            if x+1 <= N-1 and y <= N-1 and H[x+1][y] == 0:
                dfs(2, x+1, y)
            if x+1 <= N-1 and y+1 <= N-1 and H[x+1][y] == 0 and H[x][y+1] == 0 and H[x+1][y+1] == 0:
                dfs(3, x+1, y+1)

N = int(input())
H = [list(map(int, input().split(' '))) for _ in range(N)]
result = 0
dfs(1, 0, 1)
print(result)