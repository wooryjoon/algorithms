import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import copy
limit_number = 10**8
sys.setrecursionlimit(limit_number)
# DFS (각 플레이 상황에서 극한으로 돌렸을 때 count를 구해야하므로)
# 문제 정리
    # (0,0) 에서 시작
    # 동 서 남 북 으로 진행 가능.
    # 현재 위치에 써있는 값 만큼 칸 이동 가능
    # 만약 이동한 칸이 H이거나 범위를 벗어나면 (종료조건) 그때 maxx갱신
    # 무한루프가 발생하면 -1 출력
# 아이디어 
    # visited는 격자 크기만한 배열 생성
    # count와 바로 직전 자리를 기억해야함.
    # 사이클이 생성되면 무한루프 (이미 visited인곳을 가게되면 무한루프)
    # 시간을 줄이기 위해, 완탐을 하는게 아니라,DP를 활용
    # 특정 좌표 (x,y)를 거쳐간 다른 시나리오에서, 최장거리가 나왓을수도있따
    # dp배열을 통해서 (x,y)자리의 최장거리를 저장.
    # 그래서 다른 시나리오에서 거기를 가도 더 크게못한다면 아예 안가는방법
# 필요 변수
    # visited, maxx, prev, count, dx, dy
maxx = float('-inf')
flag = True
def sol() :
    n,m = list(map(int,input().split())) # 세로, 가로
    board = [list(input().strip()) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    # x,y까지 도달하는데 걸리는 가장 큰 count를 저장.
    dp = [[0]*m for _ in range(n)]

    def DFS(curr,count) :
        global maxx
        global flag
        x = curr[0]
        y = curr[1]
        visited[x][y] = 1
        step = int(board[x][y])
        for next in [(x,y+step),(x,y-step),(x+step,y),(x-step,y)]:
            nx = next[0]
            ny = next[1]
            if 0<=nx<n and 0<=ny<m and board[nx][ny] !='H' and count+1>dp[nx][ny]:
                # 위 조건을 만족하면, 돌려서 더 큰 count를 얻을 수 있다.
                if visited[nx][ny] == 1 : # 현재 시나리오에서 방문한곳이면 사이클이쥬
                    flag = False
                    return
                dp[nx][ny] = count + 1
                DFS([nx,ny],count+1)
            else :
                maxx = max(maxx,count+1)
        visited[x][y] = 0

    DFS((0,0),0) # x,y,count,prev
    if flag :
        print(maxx)
    else : print(-1)
sol()