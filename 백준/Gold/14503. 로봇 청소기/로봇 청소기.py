import sys
from collections import deque
input = sys.stdin.readline


# 문제정리
    # 1.현재칸이 청소되지 않은 경우 현재 칸 청소
    # 2.주변 4칸이 다 청소된 경우
        # 1.바라보는 방향에서 후진 가능하면 한칸 후진하고 1번 반복
        # 2. 바라보는 방향에서 뒤쪽이 벽이면 작동 멈춤
    # 3. 주변 4칸중 청소되지 않은 칸
        # 1. 반시계 방향으로 먼저 회전
        # 2. 앞쪽이 빈칸인 경우 한칸 전진 
        # 3. 1번 복귀
# 아이디어
    # 0 = 청소 안한 빈칸
    # 1 = 벽
    # 위 순서대로 돌리면서 청소한 칸 갯수 세주기

# 시간복잡도

# 변수 사용
    # cnt 
N,M = list(map(int,input().split())) # 가로 세로 
startX,startY,direction = list(map(int,input().split())) # 시작점,방향
# 방향 - > 0 : 북 1 : 동 2 : 남 3 : 서
board = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
# 
dx = [-1,0,1,0] 
dy = [0,1,0,-1]
x,y = startX,startY

while True :
    if board[x][y] == 0 :
        board[x][y] = 10
        cnt += 1
    unCleanedRoom = False
    nextDirection = False
    for i in range(4) :
        nx,ny = x+dx[i],y+dy[i]
        if board[nx][ny] == 0 :
            unCleanedRoom = True
            break
    if unCleanedRoom == True : # 청소 안 된 빈 칸 있다.
        # 북 -> 서  0 -> 3
        # 서 - 남  3 -> 2
        # 남 -> 동 2 -> 1
        # 동 -> 북 1 -> 0
        if direction == 0 : nextDirection = 3
        else : nextDirection = direction - 1
        direction = nextDirection # 방향 바꿈
        nx,ny = x+dx[direction],y+dy[direction]
        if board[nx][ny] == 0 :
            x,y = nx,ny
        continue
    else : # 사방이 다 청소된 상태
        nx,ny = x-dx[direction],y-dy[direction]
        if board[nx][ny] != 1 :
            x,y, = nx,ny
            continue
        else : break

print(cnt)