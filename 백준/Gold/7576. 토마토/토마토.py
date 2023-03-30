import sys
import copy
input = sys.stdin.readline
from collections import deque
from itertools import permutations
from sys import setrecursionlimit
setrecursionlimit(10**8)

# 

def sol() :
    n,m = list(map(int,input().split())) # 가로,세로
    tomatoes = [list(map(int,input().split())) for _ in range(m)]
    dx = (0,0,1,-1)
    dy = (1,-1,0,0)
    tomato_location = []
    def BFS(tomato_location) :
        ans = 0
        q = deque()
        for e in tomato_location:
            x,y = e
            q.append((x,y,1)) # 마지막에 1 빼줄거임

        while q :
            x,y,days = q.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0<=nx<m and 0<=ny<n and tomatoes[nx][ny] == 0 :
                    tomatoes[nx][ny] = days+1
                    q.append((nx,ny,days+1))
            ans = days
        return ans
    for i in range(m):
        for j in range(n):
            if tomatoes[i][j] == 1 : # 토마토 위치 발견
                tomato_location.append((i,j))

    ans = BFS(tomato_location)
    for arr in tomatoes:
        for e in arr :
            if e == 0 : return -1

    return ans - 1
print(sol())
