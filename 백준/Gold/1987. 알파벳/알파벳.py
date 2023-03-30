import sys
import math
import copy
input = sys.stdin.readline
from collections import deque


# BFS가 나을듯.

r,c = list(map(int,input().split()))
board = [list(input().strip()) for _ in range(r)]
dx = (0,0,1,-1)
dy = (1,-1,0,0)
maxx = -100
def DFS(x,y,count) :
    global maxx
    maxx = max(maxx,count)
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<r and 0<=ny<c :
            if hist[ord(board[nx][ny])-65] == 0 :
                hist[ord(board[nx][ny])-65] = 1
                DFS(nx,ny,count+1)
                hist[ord(board[nx][ny])-65] = 0

hist = [0] * 26
hist[ord(board[0][0])-65] = 1
DFS(0,0,1)
print(maxx)