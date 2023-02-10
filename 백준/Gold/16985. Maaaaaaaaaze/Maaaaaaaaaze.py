import sys
import copy
from collections import deque, defaultdict
from itertools import permutations
input = sys.stdin.readline

board = deque() # x, y, 층
visited = [False] * 5
ans = 9999999
dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,-1,1] # 상 하
for i in range(5):
    layer = []
    for j in range(5) :
        layer.append(list(map(int,input().split())))
    board.append(layer) 
def rotate(k):
    temp = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp[j][4-i] = newMap[k][i][j]
    return temp
def BFS () :
    global ans
    visited = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    queue = deque()
    queue.append([0,0,0])
    visited[0][0][0] = 0 # 방문 처리
    while queue :
        z,x,y = queue.popleft()
        if z == 4 and x == 4 and y == 4:
            ans = min(ans,visited[z][x][y])
        for i in range(6): # 동 서 남 북 상 하 6번
            nz,nx,ny = z+dz[i],x+dx[i],y+dy[i]
            if 0<=nz<5 and 0<=nx<5 and 0<=ny<5:
                if visited[nz][nx][ny] == -1 and newMap[nz][nx][ny] == 1:
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    queue.append([nz,nx,ny])
def DFS (newMap,depth) :
    if depth == 5:
        if newMap[4][4][4] :
            BFS()
        return
    for i in range(4) :
        if newMap[0][0][0] == 1 :
            DFS(newMap,depth+1)
        newMap[depth] = rotate(depth)

for d in permutations([0,1,2,3,4]):
    # 0,1,2,3,4를 순열로 만든 배열. ex ) 0,1,2,4,3 0,1,3,2,4
    newMap = []
    for x in d :
        newMap.append(board[x])
    DFS(newMap,0)

print(ans if ans != 9999999 else -1)
