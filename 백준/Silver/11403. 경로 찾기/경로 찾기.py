
from collections import deque;


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)] # 지도
board = [[] for _ in range(n)]
ans = [[0]*n for _ in range(n)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1 :
            board[i].append(j)
# 각 노드에서 BFS를 출발시켜서 통과하는 지점마다 ans배열에 1로 기록

def BFS (start,visited) :
    queue = deque()
    queue.append(start)
    while (len(queue)):
        currNode = queue.popleft()
        for e in board[currNode]:
            if visited[e] == True : continue
            visited[e] = True
            ans[start][e] = 1
            queue.append(e)


for i in range(0,n):
    visited = [False] * (n) # 각 노드마다 visited 초기화
    BFS(i,visited)

for e in ans:
    temp = ' '.join(map(str,e))
    print(temp)