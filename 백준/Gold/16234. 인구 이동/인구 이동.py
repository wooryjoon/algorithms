import sys
input = sys.stdin.readline
from collections import deque

# 나라를 돌면서 BFS로 연합 파악
    # 연합 국가 갯수, 연합의 인구수,연합국가의 좌표 파악
    # 각 연합 국가 인구 이동시키기.
    # 나라를 돌면서 위 연산 반복
# visited 초기화 (다음 날)


N,L,R = list(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
dx = (0,0,1,-1)
dy = (1,-1,0,0)
day = 0
def isValid(x,y,nx,ny) :
    if 0<=nx<N and 0<=ny<N:
        amount = abs(board[nx][ny] - board[x][y])
        if L<=amount<=R: 
            return True
    return False
def movePeople(location,totalPeople,totalCountry) :
    amount = totalPeople // totalCountry
    for e in location :
        x,y = e
        board[x][y] = amount

def BFS (i,j) :
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    totalPeople = board[i][j]
    totalCountry = 1
    location = [(i,j)]

    while q :
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if isValid(x,y,nx,ny) and visited[nx][ny] == 0 :
                q.append((nx,ny))
                visited[nx][ny] = 1
                totalPeople += board[nx][ny]
                totalCountry += 1
                location.append((nx,ny))
    if totalCountry == 1 : return False
    movePeople(location,totalPeople,totalCountry)
    return True




while True :
    flag = []
    visited = [[0]*N for _ in range(N)] # visited 초기화
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1 : continue
            flag.append(BFS(i,j))
    if True not in flag :
        break
    day += 1
print(day)