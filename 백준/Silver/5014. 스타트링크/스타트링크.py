import sys
import copy
input = sys.stdin.readline
from collections import deque
from itertools import permutations
from sys import setrecursionlimit
setrecursionlimit(10**8)

# 버튼을 누르는 모든 경우 완전탐색 BFS
# 

def sol() :
    F,S,G,U,D = list(map(int,input().split()))
    # S에서 G로 가기
    # 최고 높이 : F층
    visited = {}
    def BFS():
        visited[S] = 1
        q = deque()
        q.append((S,0))
        while q :
            currFloor,count = q.popleft()
            if currFloor == G :
                return count
            for nextFloor in [currFloor+U,currFloor-D]:
                if nextFloor > F or nextFloor <= 0 : continue
                if visited.get(nextFloor) : continue
                visited[nextFloor] = 1
                q.append((nextFloor,count+1))
        return 'use the stairs'
    return BFS()
print(sol())
