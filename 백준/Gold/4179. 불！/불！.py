import sys
input = sys.stdin.readline
from collections import deque

# J : 지훈이의 초기위치
# F : 불이 난 공간
# . : 지나갈 수 있는 공간
# # : 벽

# 불은 매 분 4방향으로 확산된다
# 지훈이는 미로의 끝부분에 도달하면 탈출가능
# 지훈이와 불은 벽은 못뚫는다.

# board에서 가장 빠른 탈출case
# BFS에서 J를 먼저 사방으로 보내고, 그중에 nx,ny가 도달하면 끝
# 그다음에 F를 사방으로 보낸다
dx = [0,0,1,-1]
dy = [1,-1,0,0]




r,c = list(map(int,input().split())) # 세로 가로
visited = [[0] * c for _ in range(r)]
board = [list(input().strip()) for _ in range(r)]
startJ = 0
startF = []
for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            startJ = (i,j) # J의 출발점
            board[i][j] = '.'
            continue
        if board[i][j] == 'F':
            startF.append((i,j))# 불의 출발점

def BFS (J,F,board) :
    (x,y) = J
    queue = deque()
    queue.append((x,y,"J",0))
    for x in F :
        i,j = x
        queue.append((i,j,'F',-1))
    visited[J[0]][J[1]] = 1 # 지훈이가 다녀간 자리는 방문처리
    while queue :
        x,y,types,minute = queue.popleft()
        if (x == 0 or x == r-1 or y == 0 or y == c-1) and board[x][y] =='.':
            # 이번턴에 가장자리이면서 불이안붙었다면 탈출이죠.
            return minute + 1
        for i in range(4) :
            nx,ny = x+dx[i],y+dy[i]
            if types == 'J':
                if 0<=nx<r and 0<=ny<c and board[nx][ny] == '.' and visited[nx][ny] == 0 :
                    queue.append((nx,ny,'J',minute+1))
                    visited[nx][ny] = 1
            elif types == 'F' :
                if 0<=nx<r and 0<=ny<c and board[nx][ny] == '.':
                    board[nx][ny] = 'F'
                    queue.append((nx,ny,'F',minute))
    return 'IMPOSSIBLE'


print(BFS(startJ,startF,board))