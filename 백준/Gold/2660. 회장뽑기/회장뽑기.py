from collections import deque;

n = int(input())
arr = []
while (True):
    temp = list(map(int,input().split()))
    if (temp[0] == -1): break
    arr.append(temp)
board = [[] for _ in range(n+1)]
score = [10000] * (n+1) # 각 회원의 점수

for i in range(len(arr)):
    [start,to] = arr[i]
    board[start].append(to)
    board[to].append(start)
# 각 노드에서 BFS를 출발시켜서 각 개인의 점수 기록
def BFS (start,visited) :
    visited[start] = True
    queue = deque()
    depth = 0
    queue.append([start,depth])
    while (len(queue)):
        [currNode,depth] = queue.popleft()
        for e in board[currNode]:
            if visited[e] == True : continue
            visited[e] = True
            queue.append([e,depth+1])
    return depth

for i in range(1,n+1):
    visited = [False] * (n+1)
    score[i] = BFS(i,visited)

winnerScore = min(score)
winnerCount = 0
winners = []

for i in range(len(score)):
    if score[i] == winnerScore:
        winnerCount += 1 
        winners.append(i)

print(' '.join(map(str,[winnerScore,winnerCount])))
print(' '.join(map(str,winners)))