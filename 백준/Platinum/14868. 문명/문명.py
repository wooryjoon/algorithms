import sys
from collections import deque
import copy
input = sys.stdin.readline

#문제 정리
# 입력으로 주어지는 문명의 여러 출발점
# 각 출발점에 문명의 id를 부여하고 출발 시작
# 어떤 문명이 확장중에 다른 문명을 만나면 다른 문명과 합집합 (문명 번호가 작은 쪽으로)
# parent[x] = x번문명이 속한 루트문명
# 모든 문명이 하나로 결합되는데 걸리는 최소 시간? :
# 이미 합집합인 애들을 빼고서 K-1번 이루어질 때.

N , K =  map(int,input().split())
board = [[0] * (N+1) for _ in range(N+1)]
dq = deque()
dx = (0,0,1,-1)
dy = (1,-1,0,0)
cnt = 0
for i in range(1,K+1):
    y,x = map(int,input().split())
    dq.append((i,x,y))
    board[x][y] = i
parent = [i for i in range(K+1)]

def findParent(node):
    if parent[node] != node :
        parent[node] = findParent(parent[node])
    return parent[node]

def union(a,b):
    a = findParent(a)
    b = findParent(b)
    if a <= b :
        parent[b] = a
    else :
        parent[a] = b

def BFS(dq):
    global cnt
    new = deque()
    while dq :
        type,x,y = dq.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            flag = (1<=nx<=N and 1<=ny<=N)
            if flag :
                # 미개척 땅
                if board[nx][ny] == 0 :
                    board[nx][ny] = type
                    new.append((type,nx,ny))
                    # 개척한 땅에서 인접한 노드 확인
                    for j in range(4):
                        nnx,nny = nx + dx[j], ny + dy[j]
                        nflag = (1 <= nnx <= N and 1 <= nny <= N)
                        # 인접노드 탐색 결과 이미 합집합인 그룹임
                        if nflag and board[nnx][nny] != 0 :
                            if findParent(type) == findParent(board[nnx][nny]):
                                continue
                            # 합집합이 아니라면 합쳐주기
                            union(type, board[nnx][nny])
                            cnt += 1
                # 이미 누가 먹은 땅
                else :
                    # 합집합 유무 확인
                    if findParent(type) == findParent(board[nx][ny]):
                        continue
                    # 합집합이 아니라면 합쳐주기
                    union(type,board[nx][ny])
                    cnt += 1
    return new

def init(dq):
    global cnt
    while dq :
        type,x,y = dq.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            flag = (1<=nx<=N and 1<=ny<=N)
            if flag :
                if board[nx][ny] != 0 :
                # 이미 누가 먹은 땅
                    # 합집합 유무 확인
                    if findParent(type) == findParent(board[nx][ny]):
                        continue
                    # 합집합이 아니라면 합쳐주기
                    union(type,board[nx][ny])
                    cnt += 1
# 초기값에서 모든 유니온이 형성되는 경우
year = 0
new = copy.deepcopy(dq)
init(new)

if cnt >= K - 1 :
    print(0)
else :
    while cnt < K-1 :
        year += 1
        newDq = BFS(dq)
        dq = newDq
    print(year)