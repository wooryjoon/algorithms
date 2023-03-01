import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy 

# 0 : 빈칸
# 1 : 벽
# 2 : 바이러스

# 빈칸에 벽을 3개 더 세워서 안전영역 (바이러스 침투불가영역)을 만든다.
# 벽을 3개 세우는 경우가 많겠지, 그중에 안전영역 크기의 최대값 구하기

# 조합으로 벽을 세울 수 있는 (x,y)쌍 구하기
# 구한 쌍에 벽 넣어서 새로운 board 만들기
# 만든 새로운 board에서 BFS돌려서 바이러스 침투시키기
# 바이러스 침투한 board에서 안전영역 구하기
def checkSafetyZone (board) :
    count = 0
    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 0 :
                count += 1
    return count
def extractCases (caseArr) :
    return list(combinations(caseArr,3))
def buildWall (case) :
    temp = copy.deepcopy(board)
    for x in case:
        (i,j) = x
        temp[i][j] = 1
    return temp
def BFS (newMap) :
    queue = deque()
    for x in virusLocation :
        queue.append(x)
    while queue :
        x,y = queue.popleft() # 바이러스 위치
        for i in range(4) :
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and newMap[nx][ny] == 0 :
                # 범위내 + 빈칸
                newMap[nx][ny] = 2
                queue.append((nx,ny))
    return checkSafetyZone(newMap)

n,m = list(map(int,input().split())) # 세로 가로
board = [list(map(int,input().split())) for _ in range(n)]
caseArr = []
virusLocation = []
ans = -100000
for i in range(n) :
    for j in range(m):
        if board[i][j] == 0 :
            caseArr.append((i,j))
        elif board[i][j] == 2:
            virusLocation.append((i,j))
possibleCases = extractCases(caseArr)
dx = [0,0,1,-1]
dy = [1,-1,0,0]


for x in possibleCases : # 벽세우는 경우마다 BFS
    newMap = buildWall(x) # 벽 세운 새로운 맵 생성
    # visited = [[0]*m for _ in range(n)]
    ans = max(BFS(newMap),ans)
print(ans)