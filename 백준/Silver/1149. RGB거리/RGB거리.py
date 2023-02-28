import sys
input = sys.stdin.readline
from collections import deque

# 문제 정리
    # 1번과 2번은 달라야한다
    # 연속해서 색이 같으면 안된다.
    # 결국 색이 계속해서 달라야한다
    # 
# 아이디어

#시간복잡도

n = int(input()) # 집의 갯수
cost = [list(map(int,input().split())) for _ in range(n)]
#cost[i] = [R,G,B] == i번째 집을 RGB로 색칠하는데 드는 비용

def solution (n,cost) :

    for i in range(n-1) :
        cost[i+1][0] = min(cost[i+1][0]+cost[i][1],cost[i+1][0]+cost[i][2])
        cost[i+1][1] = min(cost[i+1][1]+cost[i][0],cost[i+1][1]+cost[i][2])
        cost[i+1][2] = min(cost[i+1][2]+cost[i][1],cost[i+1][2]+cost[i][0])
    print(min(cost[n-1]))
solution(n,cost)