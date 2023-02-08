import sys
import copy
from collections import deque, defaultdict
from itertools import combinations
input = sys.stdin.readline

# 아이디어
    # 걷는다 - -1 or +1
    # 순간이동 : 2배.
    # BFS

start,end = list(map(int,input().split()))
visited = [0] * 100100
check = [0] * 100100
def history (data,time,visited) :
    arr = deque()
    for _ in range(time+1):
        arr.appendleft(data)
        data = visited[data]
    print(' '.join(map(str,arr)))

def BFS () :
    queue = deque()
    queue.append([start,0])
    visited[start] = 0
    while queue :
        curr,time = queue.popleft()
        if curr == end :
            print(time)
            history(curr,time,check)
            return 
        for i in range(3):
            if i == 0:
                n = curr + 1
            elif i == 1:
                n = curr -1
            elif i == 2:
                n = curr * 2
            if 0<=n<=100000 and visited[n] == 0:
                visited[n] = visited[curr] + 1
                queue.append([n,time+1])
                check[n] = curr

BFS()