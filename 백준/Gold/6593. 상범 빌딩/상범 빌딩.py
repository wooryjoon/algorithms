import sys
import copy
input = sys.stdin.readline
from collections import deque
from itertools import permutations
from sys import setrecursionlimit
setrecursionlimit(10**8)

# 3차원 미로에서 탈출 가능성 파악하고, 최단거리 출력(BFS)
# 불가능 하다면 Trapped!

def sol () :
    # 동 서 남 북 상 하
    dx = (0,0,1,-1,0,0)
    dy = (1,-1,0,0,0,0)
    dz = (0,0,0,0,-1,1)

    def BFS(building,visited,z,x,y,L,R,C) :
        q = deque()
        visited[z][x][y] = 1
        q.append((z,x,y,0))
        while q :
            z,x,y,time = q.popleft()
            if building[z][x][y] == 'E' :
                print("Escaped in {} minute(s).".format(time))
                return
            for i in range(6):
                nz,nx,ny = z+dz[i],x+dx[i],y+dy[i]
                if 0<= nz <L and 0<=nx<R and 0<=ny<C and building[nz][nx][ny]!='#' and visited[nz][nx][ny] == 0:
                    visited[nz][nx][ny] = 1
                    q.append((nz,nx,ny,time+1))
        print("Trapped!")
        return 

    while True :
        [L,R,C] = list(map(int,input().split())) # 높이,세로,가로
        if sum([L,R,C]) == 0 : break
        building = []
        visited = [[[0]*C for _ in range(R)] for _ in range(L)]

        for _ in range(L):
            floor = [list(input().strip()) for _ in range(R)]
            building.append(floor)
            temp = input()
        for i in range(L):
            for j in range(R):
                for k in range(C):
                    if building[i][j][k] == 'S' :
                        BFS(building,visited,i,j,k,L,R,C)

sol()