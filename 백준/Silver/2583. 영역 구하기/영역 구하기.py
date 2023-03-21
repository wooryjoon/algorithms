import sys

input = sys.stdin.readline
from collections import deque

# 문제정리
    # 모눈종이에 사각형 그리고, 공간 분할 몇군데 되는지 확인, 각 공간의 넓이도
# 아이디어
    # 1. m,n 크기의 2차원 배열을 만든다.
    # 2. papers를 돌면서 board 내에 visited 표시를 한다.
    # 3. 그후 board의 모든 좌표에서 2차원 반복문을 만든다
    # 4. visited라면 패스하고, 아니라면 BFS함수로 들어가서 
    # 5. 땅의 크기를 측정한다.
    # 6. 땅의 크기를 리턴값으로 받아 저장하여 정답을 출력한다.
# 변수 사용 계획
    # 땅count,넓이arr,BFS함수,board,사각형 색칠하는 함수
# 시간 복잡도
     
m,n,k = list(map(int,input().split())) # 가로 세로
# [x1,y1,x2,y2]
papers = [list(map(int,input().split())) for _ in range(k)]
board = [[0]*(m) for _ in range(n)]
count = 0
ansArr = []

def doVisit(location,board,m,n):
    x1,y1,x2,y2 = location
    # x1,y1 = 0,2
    # x2,y2 = 4,4
    for i in range(x1,x2):
        for j in range(y1,y2):
            board[i][j] = 1
            
def BFS (board,i,j):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque()
    size = 1
    q.append((i,j))
    board[i][j] = 1

    while q :
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<= ny <m and board[nx][ny] == 0 :
                size += 1 # 땅 발견
                board[nx][ny] = 1
                q.append((nx,ny))
    return size



for location in papers:
    doVisit(location,board,m,n)

for i in range(n):
    for j in range(m):
        if board[i][j] == 1: continue
        ansArr.append(BFS(board,i,j))
        count += 1

print(count)
ansArr.sort()
print(' '.join(map(str,ansArr)))