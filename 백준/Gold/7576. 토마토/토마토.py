import sys
input = sys.stdin.readline
from collections import deque

M,N = list(map(int,input().split())) # 가로 세로
board = [list(map(int,input().split())) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS () :
    ans = 0
    flag = False
    q = deque()
    for i in range(N):
        for j in range(M) :
            if board[i][j] == 1:
                q.append((i,j,0)) # 큐에 좌표와 소모일 넣기
    while q :
        x,y,days = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == 0:
                board[nx][ny] = 1
                q.append((nx,ny,days+1)) 
        ans = days
    for x in board :
        if 0 in x :
            flag = True
            break
    
    if flag : print(-1)
    else : print(ans)
BFS()