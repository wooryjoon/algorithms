import sys

input = sys.stdin.readline
from collections import deque

# 기울이기 동작은 벽 or 다른 구슬에 닿을때까지.
# 파란 구슬이 구멍에 빠지면 실패
# 빨간 구슬과 파란 구슬이 같은 기울이는 시점에 둘다빠지면 실패
# 10번 초과로 걸리면 -1 출력

# 아이디어
    # 두 구슬이 모두 멈출때까지 기울이며, 기울이는 방향은 동서남북 4번
    # 각 위치에서 4번씩 기울일 수 있으며, 기울이는 함수 만들자.
    # 기울일때마다 중복 방지 위해 visited에 레드블루 4좌표 모두 기록
    # BFS, 기울이는 함수 두개 필요함.
    # 종료조건 : 현재 R의 위치가 O이면서 B는 O가 아니어야함.
    # 그때 count가 10 이하이면  return count 아니면 return -1
    # B가 O위치에 도달한 경우에는 실패니까 continue

n,m = list(map(int,input().split()))
board = [list(input().strip()) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def findRB(board):
    blue,red,o = 0,0,0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'B':
                blue = (i,j);
            if board[i][j] == 'R':
                red = (i,j)
            if board[i][j] == 'O':
                o = (i,j)
    return [blue,red,o]

def slide(board,node,dx,dy) :
    cnt = 0
    x,y = node[0],node[1]
    while board[x+dx][y+dy] !='#' and board[x][y] !='O':
        x += dx
        y += dy
        cnt += 1
    return x,y,cnt

def BFS (board,blue,red,o) :
    visited = {}
    q = deque()
    q.append((blue,red,0))
    while q :
        blue,red,count = q.popleft() # 현재 지도에서 b,r위치와 횟수
        if count > 10 : return -1
        if  blue == o:
            continue
        if red == o :
            return count
        
        for i in range(4): # 4가지 방향으로 기울이면서 각 케이스 확인
            bx,by,blueCount = slide(board,blue,dx[i],dy[i])
            rx,ry,redCount = slide(board,red,dx[i],dy[i])
            if (bx,by) == (rx,ry): # 같은 위치에 있다면?
                if (bx,by) == o : # 둘다 구멍에 빠진거라면?
                    continue # 이 case에선더 볼게 없으므로 넘어간다.

                if blueCount > redCount : # 파랭이가 더 많이갔니?
                    bx = bx-dx[i]
                    by = by-dy[i]
                else :
                    rx = rx-dx[i]
                    ry = ry-dy[i]

            key = ''.join(map(str,[bx,by,rx,ry]))
            if not visited.get(key) :
                # 중복이 아니라면?
                visited[key] = 1
                q.append(((bx,by),(rx,ry),count+1))
    return -1

blue,red,o = findRB(board) # 초기 파랑,빨강,원점 찾기
print(BFS(board,blue,red,o))