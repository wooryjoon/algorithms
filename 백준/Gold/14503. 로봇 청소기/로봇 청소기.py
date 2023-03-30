import sys
from collections import deque
input = sys.stdin.readline


# 문제정리
    # 1.현재 칸이 청소되지 않은 경우 현재 칸 청소(방문 처리)
    # 2.주변 4칸이 청소할 곳이 없는 경우
        # 1.바라보는 방향에서 후진 가능하면(뒤쪽 벽x) 한칸 후진하고 1번 반복
        # 2. 바라보는 방향에서 뒤쪽이 벽이면 작동 멈춤
    # 3. 주변 4칸중 청소할 곳이 있는 경우
        # 1. 로봇 청소기를 반시계 방향으로 먼저 회전(ok)
        # 2. 앞쪽이 빈칸인 경우 한칸 전진  (ok)
        # 3. 1번 복귀 (ok)
# 아이디어 BFS
    # 0 = 청소 안한 빈칸
    # 1 = 벽
    # 위 순서대로 돌리면서 청소한 칸 갯수 세주기
    # 로봇청소기가 방향을 갖고있다. -> 바라보는 방향을 계속 인지해야한다.


N,M = list(map(int,input().split())) # 가로 세로 
startX,startY,direction = list(map(int,input().split())) # 시작점,방향
# 방향 - > 0 : 북 1 : 동 2 : 남 3 : 서

board = [list(map(int,input().split())) for _ in range(N)]

cnt = 0 # 정답 출력할 변수  == 청소하는 칸의 개수

# 북 동 남 서
dx = [-1,0,1,0] 
dy = [0,1,0,-1]
x,y = startX,startY

while True :
    # 최초 로봇청소기의 위치에서, 청소되지 않은 칸.
    if board[x][y] == 0 : # 1번 연산
        board[x][y] = 10 # 청소된 칸.
        cnt += 1
    unCleanedRoom = False
    nextDirection = False
    for i in range(4) :
        nx,ny = x+dx[i],y+dy[i]
        if board[nx][ny] == 0 : # 청소할 칸이 있따.
            unCleanedRoom = True
            break
    if unCleanedRoom == True : # 청소 안 된 빈 칸 있다.
        #반시계 회전.
        # 북 -> 서  0 -> 3
        # 서 - 남  3 -> 2
        # 남 -> 동 2 -> 1
        # 동 -> 북 1 -> 0
        if direction == 0 : nextDirection = 3
        else : nextDirection = direction - 1
        direction = nextDirection # 방향 바꿈
        nx,ny = x+dx[direction],y+dy[direction] # 전진
        if board[nx][ny] == 0 : # 청소할 수 있는 경우.
            x,y = nx,ny # 진짜로 전진한다.
        continue
    else : # 사방이 다 청소된 상태
        nx,ny = x-dx[direction],y-dy[direction] # 바라보는 방향 기준 한칸 후진한 좌표
        if board[nx][ny] != 1 : # 후진한 칸이 벽이 아니라면
            x,y = nx,ny # 진짜로 후진한다.
            continue # 다시 1번 수행으로 돌아간다.
        else : break # 후진을 할수 없다면
        
print(cnt)