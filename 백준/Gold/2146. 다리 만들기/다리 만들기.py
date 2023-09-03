import sys
from collections import deque
input = sys.stdin.readline

# 입력 사이즈
    # N : 100 이하의 자연수
# 문제 정리
    # N * N 지도에 여러개의 대륙이 존재
    # 한 대륙과 다른 한 대륙 사이를 이을 수 있는 가장 짧은 길이의 다리 찾기
# How To Solve?

    # 1. 입력
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
    # 2. 필요 변수 선언 :ans, visited, BFS_func
ans = 99999999
visited = [[0] * N for _ in range(N)]
location = [[] for _ in range(N * N + 1)]
dx = (0,0,1,-1)
dy = (1,-1,0,0)

def BFS(ground,type) :
    global ans
    # BFS
    q = deque()
    for e in ground :
        x,y = e
        p = (x,y,0)
        q.append(p)
    while q :
        x,y,length = q.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            # 범위 체크
            if 0<=nx<N and 0<=ny<N:
                # 주변 노드가 방문한 땅이면 x
                if visited[nx][ny] == 1: continue
                # 주변 노드가 같은 땅이면 x
                if board[nx][ny] == type : continue
                # 주변 노드가 빈칸이면 다리 길이 + 1, 방문 처리 하고 큐에 넣기
                if board[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny,length + 1))
                # 주변 노드가 다른 땅이면? -> 정답 갱신 후 바로 리턴
                if board[nx][ny] > 0 :
                    ans = min(ans,length)
                    return
def grouping(x,y,team) :
    q = deque()
    visited[x][y] = 1
    q.append((x,y))
    while q :
        x,y = q.popleft()
        board[x][y] = team
        location[team].append((x,y))
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N :
                if visited[nx][ny] == 1 : continue
                if board[nx][ny] == 1:
                    q.append((nx,ny))
                    visited[nx][ny] = 1


# 3. 지도를 2중 For문으로 순회하며, 대륙마다 그룹핑
team = 0
for i in range(N) :
    for j in range(N):
        if visited[i][j] == 1 : continue
        if board[i][j] == 0 : continue
        team += 1
        grouping(i,j,team)
# 4. 각 그룹마다 한번씩 자기 땅의 모든 칸에서 BFS 출발
for i in range(1,team + 1) :
    visited = [[0] * N for _ in range(N)]
    BFS(location[i],i)
# 5. ans 변수 갱신 후 정답 출력
print(ans)






