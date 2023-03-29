import sys
import copy
input = sys.stdin.readline
from collections import deque
from itertools import permutations

# 나이트는 현재 위치에서 최대 8개의 위치로 이동 가능
# dx,dy로 케이스 분류해서 기록
# 

def sol () :
    T = int(input())
    dx = (-1,-2,-2,-1,1,2,2,1)
    dy = (-2,-1,1,2,2,1,-1,-2)
    ans = []
    def BFS(start,board,end):
        x,y = start
        q = deque()
        board[x][y] = 1
        q.append((x,y,0))
        while q :
            x,y,count = q.popleft()
            if end == (x,y):
                return count
            for i in range(8):
                nx,ny = x+dx[i],y+dy[i]
                if 0<=nx<I and 0<=ny<I and board[nx][ny] == 0 :
                    board[nx][ny] = 1
                    q.append((nx,ny,count+1))

    for i in range(T):
        I = int(input())
        start = tuple(map(int,input().split()))
        end = tuple(map(int,input().split()))
        board = [[0]*I for _ in range(I)]
        ans.append(BFS(start,board,end))
    print('\n'.join(map(str,ans)))
sol()