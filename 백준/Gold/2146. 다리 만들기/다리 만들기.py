# 각 섬을 -1로 표시하고, 섬의 모든 칸에서 BFS로 표시하면서 나아가기
# 나아가면서 겹치는곳은 방문 안하게 해놓고, 인접노드가 -1인곳을 만나면, 그대로 리턴
from collections import deque
import copy
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)] 

dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = []
cnt = 2
def BFS (i,j,value) :
    queue = deque()
    queue.append([i,j,0])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[i][j] = True # BFS 내에서 따로 체크를 위한 복사맵
    while (queue):
        [x,y,count] = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위벗어나거나, 이미방문한칸이거나, 같은섬이면 패스
            if (nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny] == True or map[nx][ny] == value):
                continue
            if (map[nx][ny] == 0) : 
                # 인접한 칸이 바다일 때
                queue.append([nx,ny,count + 1])
                visited[nx][ny] = True
            elif (map[nx][ny] != 0 and map[nx][ny] != value): # 인접한 칸이 바다도 아니고, 자기랑 연결된 자기섬도 아닐때 즉, 다른섬
                answer.append(count)
                return

# 섬에 id부여하는 함수
def BFS2 (i,j,cnt) :
    queue = deque()
    queue.append([i,j])
    map[i][j] = cnt
    while(queue):
        [x,y] = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx >= 0 and ny >= 0 and nx < n and ny < n and map[nx][ny] == 1):
                queue.append([nx,ny])
                map[nx][ny] = cnt

# 각 떨어진 섬들마다 id 부여
map = copy.deepcopy(board)
for i in range(n) : 
    for j in range(n):
        if (map[i][j] == 1) : 
            BFS2(i,j,cnt)
            cnt = cnt + 1

# 중첩 반복을 통해 최단거리 찾기
for i in range(n):
    for j in range(n):
        if (board[i][j] > 0):
            BFS(i,j,map[i][j])
print(min(answer))

