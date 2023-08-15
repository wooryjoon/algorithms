import sys
input = sys.stdin.readline
from heapq import heappop,heappush
from collections import deque


# 아이디어
    # 봄 여름 가을 겨울에 일어나는 일을 순차적으로 적용

# N = board크기, M : 나무 개수  K : K년 지난 후
N,M,K = list(map(int,input().split()))
energy = [[5]*N for _ in range(N)]
treeBoard = [[deque() for _ in range(N)] for _ in range(N)]
# 각 땅마다 매년 추가되는 양분의 값을 담은 배열
plus = [list(map(int,input().split())) for _ in range(N)]
# 나무의 정보
trees = deque()
deadTrees = []
dx = (0,0,1,-1,-1,-1,1,1)
dy = (1,-1,0,0,-1,1,-1,1)
ans = 0
for i in range(M):
    # 좌표,좌표, 나이
    x,y,z = list(map(int,input().split()))
    # 최초 나무 위치 설정
    treeBoard[x-1][y-1].append(z)
# K년 동안 반복
for _ in range(K):
    # 봄, 여름
    for i in range(N):
        for j in range(N):
            # 나무가 존재하면?
            if len(treeBoard[i][j]) > 0 :
                while len(treeBoard[i][j]) > 0 :
                    # 나이가 제일 어린 나무의 나이
                    if energy[i][j] - treeBoard[i][j][0] < 0:
                        break
                    currAge = treeBoard[i][j].popleft()
                    energy[i][j] -= currAge
                    trees.append([i,j,currAge+1])
                # While문 종료 -> 양분 못먹은 나무가 남은 경우
                if len(treeBoard[i][j]) > 0 :
                    while len(treeBoard[i][j]):
                        z = treeBoard[i][j].pop()
                        energy[i][j] += z // 2
            energy[i][j] += plus[i][j]
    # 가을
    for e in trees :
        x,y,z = e
        treeBoard[x][y].append(z)
    while trees :
        # 나이 어린애부터 나온다
        x,y,z = trees.pop()
        if z % 5 == 0 :
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    treeBoard[nx][ny].appendleft(1)

for i in range(N):
    for j in range(N):
        ans += len(treeBoard[i][j])

print(ans)




