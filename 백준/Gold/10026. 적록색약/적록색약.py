import sys
import copy
input = sys.stdin.readline
from collections import deque
from itertools import permutations
from sys import setrecursionlimit
setrecursionlimit(10**8)

# board를 두개 만들어서, 적록색약ver, 정상ver 두개로 BFS 돌린다.


def sol () :
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    dx = (0,0,1,-1)
    dy = (1,-1,0,0)
    ans = []

    def BFS(x,y,color,visited):
        q = deque()
        visited[x][y] = 1
        q.append((x,y))
        while q :
            x,y = q.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and board[nx][ny] == color:
                    q.append((nx,ny))
                    visited[nx][ny] = 1

    # 정상 버전
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1: continue
            BFS(i,j,board[i][j],visited)
            cnt += 1
    ans.append(cnt)

    # 적록색약 
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'R':
                board[i][j] = 'G'

    # 적록색약 버전
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1: continue
            BFS(i,j,board[i][j],visited)
            cnt += 1
    ans.append(cnt)
    print(' '.join(map(str,ans)))
sol()