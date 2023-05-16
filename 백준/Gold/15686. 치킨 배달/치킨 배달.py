
from itertools import combinations
N,M = list(map(int,input().split())) # 마을크기, 최대 치킨집 개수
board = [list(map(int,input().split())) for _ in range(N)] # 마을 정보
chickens = []
houses = []
maxxy = 10**8

def extractDist (location,chicken) :
    result = 10**8
    x,y = location
    # 전체를 돌면서 치킨집이 나올때마다 거리 측정
    for e in chicken :
        currDist = abs(x-e[0]) + abs(y-e[1])
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
    for e in houses:
        totalChickenDist += extractDist(e,chicken)
    maxxy = min(maxxy,totalChickenDist)

print(maxxy)