from collections import deque
import sys
input = sys.stdin.readline

# 시작칸 끝칸 포함, 0,0에서 출발. -> (n-1,m-1)에서 도착
# 벽 K개까지 부수고 도착하는 시나리오 가능
# 각 좌표의 visited는 길이가 K+1인 배열로.
# ex) if k == 4 -> visited[3][5] = [0,0,0,0]
# Memoization

n,m,k = list(map(int,input().split()))
board = [list(input().strip()) for _ in range(n)]
dx = (1,0,-1,0) # 남 동 북 서
dy = (0,1,0,-1) # 남 동 북 서

visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]

def BFS():
    visited[0][0][0] = 1 # 시작점 방문처리
    q = deque()
    q.append((0,0,0,1)) # x,y,벽 부순 횟수,지나온 경로의 길이

    while q :
        x,y,broken,dist = q.popleft()  # x,y,벽 부순 횟수,지나온 경로의 길이
        if x == n-1 and y == m-1 : # 도착점에 도달한 Node라면
            return dist
        
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            # 다음 칸이 범위 내에 있고, 
            # 벽을 broken번 깬 시나리오에서 도달하지 않은 지점이고, 
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny][broken] : 
                # 1. 다음 칸이 벽인 경우
                if board[nx][ny] == '1' :  # 만약 벽을 부술 기회가 남은 경우 부시고 간다.
                    if broken < k and not visited[nx][ny][broken+1] :
                        q.append((nx,ny,broken+1,dist+1))
                        visited[nx][ny][broken+1] = 1

                # 2. 다음 칸이 벽이 아닌 경우
                elif board[nx][ny] == '0':# 벽을 안부수고 그냥 간다.
                    q.append((nx,ny,broken,dist+1))
                    visited[nx][ny][broken] = 1
    return -1

print(BFS())