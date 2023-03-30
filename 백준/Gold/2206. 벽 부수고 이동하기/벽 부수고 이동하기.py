import sys
import copy
input = sys.stdin.readline
from collections import deque
from itertools import permutations
from sys import setrecursionlimit
setrecursionlimit(10**8)

# visited의 각 칸을 벽을 부순경우의 visit과 안 부순 경우의 visit
# 칸 개수는 시작경로부터 센다.
# 0,0에서 출발, n-1,m-1에 도달
n,m = list(map(int,input().split()))
board = [list(input().strip()) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = (0,0,1,-1)
dy = (1,-1,0,0)

def BFS () :
    q = deque()
    visited[0][0][0] = 1 # 찬스 안 쓴 상태로 방문처리
    q.append((0,0,1,0))
    while q :
        x,y,cnt,chance = q.popleft()
        if x == n-1 and y == m-1 :
            return cnt
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m: # 범위 조건
                if chance == 1 : # 찬스 쓴 경우
                    if board[nx][ny] == '1': # 벽 만나면 못 뚫음
                        continue
                    elif board[nx][ny] == '0' and visited[nx][ny][chance] == 0 :
                        visited[nx][ny][chance] = 1
                        q.append((nx,ny,cnt+1,chance))
                elif chance == 0 : # 찬스 안 쓴 경우
                    if board[nx][ny] == '1': # 벽 만남
                        visited[nx][ny][chance+1] = 1
                        q.append((nx,ny,cnt+1,chance+1))
                    elif board[nx][ny] == '0' and visited[nx][ny][chance] == 0 : # 벽 안만남
                        visited[nx][ny][chance] = 1
                        q.append((nx,ny,cnt+1,chance))
    return -1
print(BFS())