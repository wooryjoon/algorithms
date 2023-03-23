import sys
import copy
input = sys.stdin.readline
from collections import deque

# 합이 최대가 되려면?
    # board를 하루가 지날떄마다 수정하는 함수
    # L이 서로 만날 수 있는지 BFS로 확인하는 함수 필요
    # meltingTime 2차원 배열에 각 칸이 몇일 뒤 녹는지 기록해놓는다.
    # 모든 얼음이 다 녹는 그 순간의 요일을 max로 설정
    # minn = 0 max = 위에서 구한값.
    # mid 시점에서 BFS를 돌려서 start가 end에 닿으면 return True

r,c = list(map(int,input().split()))
board = [list(input().strip()) for _ in range(r)]
day = 0
waterSpots = []
swanSpots = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
meltingTable = [[0]*c for _ in range(r)]

for i in range(r): # 백조, 물 첫 위치 기록
    for j in range(c):
        if board[i][j] == '.':
            waterSpots.append((i,j))
        if board[i][j] == 'L':
            swanSpots.append((i,j))
            waterSpots.append((i,j))
start = swanSpots[0]
end = swanSpots[1]

def watering (board,waterSpots,days) :
    new = []
    for e in waterSpots :
        x,y = e
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < r and 0<= ny < c and board[nx][ny] == 'X':
                new.append((nx,ny))
                meltingTable[nx][ny] = days
                board[nx][ny] = '.'

    if len(new): # 더 진행 가능하다.
        return new
    return False

def extractMaxDay (board) :
    days = 0
    temp = copy.deepcopy(board)
    waterTemp = copy.deepcopy(waterSpots)

    while True :
        waterTemp = watering(temp,waterTemp,days+1)
        if not waterTemp : break
        days += 1

    return days

def BFS (board,currDay) :
    q = deque()
    q.append(start)
    visited = [[0]*c for _ in range(r)]
    x,y = start[0],start[1]
    visited[x][y] = 1
    while q :
        x,y = q.popleft()
        if x == end[0] and y == end[1] : return True
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<r and 0<=ny<c:
                if visited[nx][ny] == 1 : continue

                if meltingTable[nx][ny] <= currDay :
                    # 현시점 날짜에 녹아있는가?
                    visited[nx][ny] = 1
                    q.append([nx,ny])
    return False

minn = 0
maxx = extractMaxDay(board)
answer = -10
# 이분 탐색
while minn <= maxx :
    mid = (minn+maxx) // 2 # 기준 day
    flag = BFS(board,mid)

    if flag : # 만남
        maxx = mid - 1
        answer = mid
    else : # 못 만남
        minn = mid + 1
print(answer)
