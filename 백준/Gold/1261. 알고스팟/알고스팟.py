import sys
input = sys.stdin.readline
from collections import deque
# 문제 정리
    # 2차원배열에서 동서남북으로 벽을 부시며 이동
    # 0,0 위치에서 N,M 으로 이동하기 위해 벽을 최소로 부시는 경우를 구하는 문제
# 아이디어
    # BFS
    # 3차원 visited 배열
    # 효율적 연산을 위한 아이디어
M,N = list(map(int,input().split())) # 가로, 세로
board = [list(input().strip()) for _ in range(N)] # board 생성
dx = (0,0,1,-1)
dy = (1,-1,0,0)
def BFS() :
    q = deque()
    # visited[x][y][z] = x,y에 z번 부순 case로 도달한 경우
    visited = [[[0] * (201) for _ in range(M)] for _ in range(N)]
    q.append((0,0,0))
    visited[0][0][0] = 1
    dp = [[float('inf')] * M for _ in range(N)]
    dp[0][0] = 0

    while q :
        x,y,count = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if not (0<=nx<N and 0<=ny<M) : continue
            if count >= dp[nx][ny] : continue

            if board[nx][ny] == '0' :
                if visited[nx][ny][count] == 0 :
                    visited[nx][ny][count] = 1
                    q.append((nx,ny,count))
                    dp[nx][ny] = count
            elif board[nx][ny] == '1' :
                if visited[nx][ny][count+1] == 0 :
                    visited[nx][ny][count+1] = 1
                    q.append((nx,ny,count+1))
                    dp[nx][ny] = count+1
    return dp[N-1][M-1]
print(BFS())



