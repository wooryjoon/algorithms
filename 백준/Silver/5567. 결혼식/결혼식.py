
from collections import deque;


n = int(input())
m = int(input())
arr = [list(map(int,input().split())) for _ in range(m)]
board = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    [start,to] = arr[i]
    board[start].append(to)
    board[to].append(start)

def BFS (start) :
    visited[start] = 100
    queue = deque()
    queue.append([start,0])
    while(len(queue)):
        [curr,depth] = queue.popleft()
        for e in board[curr]:
            if visited[e] >0 : continue
            visited[e] =depth+1
            queue.append([e,depth+1])
    

BFS(1)
count = 0
for e in visited:
    if e > 0 and e <=2:
        count += 1
print(count)