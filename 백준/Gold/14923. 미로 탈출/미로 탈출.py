import sys
input = sys.stdin.readline
from collections import deque

# 미로, 탈출위치 안다.
# 벽 있다.
# 벽을 길로 만들 수 있는데, 한번만 사용 가능
# 가장 빠른 탈출 경로의 거리를 구하라.
# maze에 0은 빈칸, 1은 벽이다.
N,M = list(map(int,input().split())) # 미로 세로 가로
Hx,Hy = list(map(int,input().split())) # 시작점
Ex,Ey = list(map(int,input().split())) # 탈출점
maze = [list(map(int,input().split())) for _ in range(N)] # 미로
dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited = [[[0,0] for _ in range(M)] for _ in range(N)] # [방문여부,지팡이 사용여부]

def BFS () :
    queue = deque()
    queue.append([Hx-1,Hy-1,0,1])
    visited[Hx-1][Hy-1][1] = 1 # 방문 처리
    while queue :
        x,y,dist,isUsed = queue.popleft()

        if x == Ex-1 and y == Ey-1 :
            return dist
        
        for i in range(4) :
            nx,ny = x+dx[i],y+dy[i]

            if 0<=nx<N and 0<=ny<M and visited[nx][ny][isUsed] == 0 :
                if isUsed and maze[nx][ny]:
                    visited[nx][ny][0] = 1
                    queue.append([nx,ny,dist+1,0])
                elif not maze[nx][ny]:
                    visited[nx][ny][isUsed] = 1
                    queue.append([nx,ny,dist+1,isUsed])
    return -1
print(BFS())

