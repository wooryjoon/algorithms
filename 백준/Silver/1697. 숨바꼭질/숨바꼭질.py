import sys
import copy
input = sys.stdin.readline
from collections import deque

# BFS로 시간 카운트하면서 출발
# K에 도달했을 때 그때의 시간 리턴.

def sol () :
    n,k = list(map(int,input().split()))
    visited = {}
    def BFS():
        q = deque()
        q.append((n,0)) # 현재위치, 현재까지 소요시간
        visited[n] = 1
        while q :
            curr,time = q.popleft()
            if curr == k :
                return time
            for e in [curr+1,curr-1,curr+curr]:
                if e > 100000: continue
                if visited.get(e) : continue
                visited[e] = 1
                q.append((e,time+1))
    print(BFS())
sol()