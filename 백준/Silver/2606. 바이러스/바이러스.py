
from collections import deque;


n = int(input())
m = int(input())
arr = [list(map(int,input().split())) for _ in range(m)]
board = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    [start,to] = arr[i]
    board[start].append(to)
    board[to].append(start)

def BFS (start) :
    count = 0
    queue = deque()
    queue.append(start)
    while(len(queue)):
        curr = queue.popleft()
        for e in board[curr]:
            if visited[e] == True : continue
            visited[e] = True
            count += 1
            queue.append(e)
    return count

visited[1] = True
print(BFS(1))
