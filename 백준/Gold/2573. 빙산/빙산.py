# 각 배열의 요소는 빙산의 높이
# 빙산이 없는 경우는 0
# 빙산의 높이 감소는 동서남북으로 0이 몇개인지에 따라 비례적으로 감소함
# 한덩어리의 빙산이 두 덩어리 이상으로 분리되는 최초의 시간을 구하라.
# 이중 반복을 통해 1년마다 map을 갱신한다.
# 갱신된 map을 DFS 함수에 넣어서, 분리된 빙산의 개수를 파악한다.
# 빙산 분리가 2개이상이 되는 최초 시점에 time을 리턴한다.
import copy
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]
[n,m] = list(map(int,input().split())) # n(n), m(m) 설정
maps = [list(map(int,input().split())) for _ in range(n)] # map설정완료
def BFS (x,y,visited):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 0
    while (queue):
        [nx,ny] = queue.popleft()
        for i in range(4):
            nxx = nx + dx[i]
            nyy = ny + dy[i]
            if (nxx >= 0 and nyy >= 0 and nxx < n and nyy < m and visited[nxx][nyy] != 0):
                visited[nxx][nyy] = 0
                queue.append([nxx,nyy])
        
    
def isSeperate (board) :
    visited = copy.deepcopy(board)
    count = 0
    for q in range(n):
        for p in range(m):
            if (visited[q][p] != 0) : 
                count  = count + 1
                BFS(q,p,visited)
    return count
    
time = 0
while (isSeperate(maps) == 1):
    copymaps = copy.deepcopy(maps)
    time = time + 1
    for i in range(n):
        for j in range(m):
            if (maps[i][j] == 0): continue
            currNode = maps[i][j] # 해당 노드의 높이
            waveCount = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if (nx >= 0 and ny >= 0 and nx < n and ny < m and maps[nx][ny] == 0):
                    waveCount = waveCount + 1 #최소한 0
            copymaps[i][j] = max(currNode-waveCount,0)
    maps = copymaps
    # 모든 칸에 대해 연산 수행 후
if (isSeperate(maps) == 0) : print(0)
else : print(time)