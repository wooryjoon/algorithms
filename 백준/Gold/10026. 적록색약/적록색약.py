# 결국 상하좌우 탐색하면서 역시 BFS로 푸는 문제이다
# 적록색약인 사람의 경우에는 G를 다 R로 바꾸어주고 같은 BFS를 돌린다.
from collections import deque
import copy

N = int(input())
map = []
for i in range(N):
    lines = list(input())
    map.append(lines) # map 구현 완료
# map = [
#     ['R','R','R','B','B'],
#     ['G','G','B','B','B'],
#     ['B','B','B','R','R'],
#     ['B','B','R','R','R'],
#     ['R','R','R','R','R']
# ]
newMap = copy.deepcopy(map) # 배열 깊은 복사
for i in range(len(newMap)):
    for j in range(len(newMap[0])):
        if (newMap[i][j] == 'G'): newMap[i][j] = 'R'
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS (row,col,visited):
    target = visited[row][col]
    visited[row][col] = -1
    queue = deque();
    queue.append([row,col])
    while (len(queue)):
        [x,y] = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx >= 0 and ny >= 0 and nx < len(visited) and ny < len(visited[0])):
                if (visited[nx][ny] == target):
                    queue.append([nx,ny])
                    visited[nx][ny] = -1 # 주의점 : nx ny 가 범위값을 벗어나는데, 그 값으로 조건문 돌리려고해서 오류남

# 일반 map bfs연산
count = 0
for i in range(len(map)): 
    for j in range(len(map[0])):
        if (map[i][j] != -1):
            count += 1
            BFS(i,j,map)
print(count)

# 적록색맹 bfs연산
count = 0
for i in range(len(newMap)): 
    for j in range(len(newMap[0])):
        if (newMap[i][j] != -1):
            count += 1
            BFS(i,j,newMap)
print(count)


