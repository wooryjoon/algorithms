import sys
from collections import deque;


n,m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

board = [[] for _ in range(n+1)];
visited = [False] * (n+1);
queue = deque();
count = 0

for i in range(m):
    [start,to] = arr[i];
    board[start].append(to);
    board[to].append(start); # 양쪽에 넣어주기

def BFS(start):
    visited[start] = True
    queue.append(start);
    while (len(queue)) :
        nextNode = queue.popleft()
        for e in board[nextNode]:
            if (visited[e] == True): continue
            visited[e] = True
            queue.append(e);
    return;
    
    

for i in range(1,n+1):
        if visited[i] == False: # 방문 안한 노드이면
            count += 1
            BFS(i)
print(count);
