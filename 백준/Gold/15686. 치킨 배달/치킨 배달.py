# 문제 정리
    # 치킨거리 = 집에서 가장 가까운 치킨집 사이의 거리
    # 도시의 치킨거리 = 모든 치킨거리의 합
    # 도시 치킨거리의 최솟값 구하기

# 아이디어
    # 치킨집 총 개수 중 M개를 뽑아서 해당 좌표값을 -1로 만든다. (-1 == 살아있는 치킨집)
    # 각 집에서 BFS를 돌려서 치킨 거리를 구한다.
    # 해당 분기점의 도시의 치킨거리를 구해주고, maxx값을 갱신해준다.
from itertools import combinations
from collections import deque
N,M = list(map(int,input().split())) # 마을크기, 최대 치킨집 개수
board = [list(map(int,input().split())) for _ in range(N)] # 마을 정보
chickens = []
houses = []
maxxy = 10**8
dx = (0,0,1,-1)
dy = (1,-1,0,0)

def BFS (location) :
    result = 10**8
    x,y = location
    # 전체를 돌면서 치킨집이 나올때마다 거리 측정
    for i in range(N):
        for j in range(N):
            if board[i][j] == -1 :
                currDist = abs(x-i) + abs(y-j)
                result = min(result,currDist)
    return result





#치킨집 ,집 좌표 따기
for i in range(N):
    for j in range(N):
        if board[i][j] == 2 :
            chickens.append((i,j))
        if board[i][j] == 1 :
            houses.append((i,j))

# 살릴 치킨집 고르는 모든 경우 담기
pickedChickens = list(combinations(chickens,M))

# 매 시나리오마다 확인
for chicken in pickedChickens :
    totalChickenDist = 0
    for e in chicken :
        x,y = e
        board[x][y] = -1
    for e in houses:
        totalChickenDist += BFS(e)
    maxxy = min(maxxy,totalChickenDist)
    for e in chicken :
        x,y = e
        board[x][y] = 2
print(maxxy)