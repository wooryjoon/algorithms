from collections import deque
import sys
input = sys.stdin.readline

def BFS (currNode,visited,board) : # 맨첨에 1넣기
    queue = deque()
    visited[currNode] = 1
    queue.append([currNode,1])
    while (len(queue)):
        [node,value] = queue.popleft()
        for e in board[node]:
            if visited[e] == value : return False 
            if  visited[e] == 0 :
                visited[e] = -value
                queue.append([e,-value])
    return True

T =int(input()) # 테케 갯수
ans = []
for _ in range(T):
    [n,m] =list(map(int,input().split()))  #노드의 개수, 간선의 개수
    arr = [list(map(int,input().split())) for _ in range(m)]
    board = [[] for _ in range(n+1)]  
    visited = [0] * (n+1)
    for e in arr: # board 작성
        [start,to] = e
        board[start].append(to)
        board[to].append(start)
    flag = True
    for i in range(1,n+1):
        if visited[i] == 0:
            flag = BFS(i,visited,board)
            if flag == False: break
    if flag == True :ans.append('YES')
    else: ans.append('NO')

for e in ans:
    print(e)