# CCTV는 벽 통과 못함
# CCTV는 CCTV를 통과할 수 있다.
# 6 : 벽, 0 : 빈칸 1~5 : CCTV
# 각 CCTV가 비출 수 있는 모든 경우 완전탐색
from copy import deepcopy
def top(board,x,y):
    for nx in range(x - 1, -1, -1):
        if board[nx][y] == 0:
            board[nx][y] = '#'
        elif board[nx][y] == 6:
            return
    return
def right(board,x,y) :
    for ny in range(y+1,M):
        if board[x][ny] == 0 :
            board[x][ny] = '#'
        elif board[x][ny] == 6 :
            return
    return
def bottom(board,x,y) :
    for nx in range(x+1,N):
        if board[nx][y] == 0 :
            board[nx][y] = '#'
        elif board[nx][y] == 6 :
            return
    return
def left(board,x,y) :
    for ny in range(y-1,-1,-1):
        if board[x][ny] == 0 :
            board[x][ny] = '#'
        elif board[x][ny] == 6 :
            return
    return
def CCTV1 (board,x,y,direction) :
    # 상 우 하 좌
    if direction == 0 : #상
        top(board,x,y)
    if direction == 1 : #우
        right(board,x,y)
    if direction == 2 : #하
        bottom(board,x,y)
    if direction == 3 : #좌
        left(board,x,y)
def CCTV2 (board,x,y,direction) :
    if direction == 0 : #상 하
        top(board,x,y)
        bottom(board,x,y)
    if direction == 1 : #좌 우
        right(board,x,y)
        left(board,x,y)
def CCTV3 (board,x,y,direction) :
    if direction == 0 : #상 우
        top(board,x,y)
        right(board,x,y)
    if direction == 1 : #우 하
        right(board,x,y)
        bottom(board,x,y)
    if direction == 2 : #하 좌
        bottom(board,x,y)
        left(board,x,y)
    if direction == 3 : #좌 상
        left(board,x,y)
        top(board,x,y)
def CCTV4 (board,x,y,direction) :
    if direction == 0 : #좌 상 우
        left(board,x,y)
        top(board,x,y)
        right(board,x,y)
    if direction == 1 : #상 우 하
        top(board,x,y)
        right(board,x,y)
        bottom(board,x,y)
    if direction == 2 : #우 하 좌
        right(board,x,y)
        bottom(board,x,y)
        left(board,x,y)
    if direction == 3 : #하 좌 상
        bottom(board,x,y)
        left(board,x,y)
        top(board,x,y)
def CCTV5 (board,x,y):
    bottom(board, x, y)
    left(board, x, y)
    right(board,x,y)
    top(board, x, y)
def check(board) :
    cnt = 0
    for arr in board :
        for e in arr :
            if e == 0 :
                cnt += 1
    return cnt
def DFS (board,depth) :
    global result
    if depth == len(CCTV_location) :
        result = min(result,check(board))
        return
    x,y = CCTV_location[depth]
    CCTV_Type = board[x][y]
    if CCTV_Type == 1 :
        for i in range(4):
            copy = deepcopy(board)
            CCTV1(copy,x,y,i)
            DFS(copy,depth+1)
    elif CCTV_Type == 2 :
        for i in range(2):
            copy = deepcopy(board)
            CCTV2(copy, x, y, i)
            DFS(copy, depth + 1)
    elif CCTV_Type == 3 :
        for i in range(4):
            copy = deepcopy(board)
            CCTV3(copy,x,y,i)
            DFS(copy,depth+1)
    elif CCTV_Type == 4:
        for i in range(4):
            copy = deepcopy(board)
            CCTV4(copy, x, y, i)
            DFS(copy, depth + 1)
    elif CCTV_Type == 5:
        copy = deepcopy(board)
        CCTV5(copy,x,y)
        DFS(copy,depth+1)


N,M = list(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
CCTV_location = []
result = 10000

# CCTV가 위치한 좌표 저장
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5 :
            CCTV_location.append((i,j))


DFS(board,0)
print(result)