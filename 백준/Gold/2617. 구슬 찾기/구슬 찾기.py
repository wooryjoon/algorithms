import sys
from collections import deque
input = sys.stdin.readline
# 문제 정리
    # 총 n개일 떄 자식이 몇개 이상, 몇개 이하면 중간이 불가능한가?
    # 자식이 (n//2 + 1) 이상이면 중간 불가.
    # 자식이 (n//2 -1) 이하면 중간 불가
    # n == 5  -> 자식 3명 이상, 1명 이하
    # n == 7 ->  1 2 3 4 5 6 7
    # 자식 4명 이상 ,2명 이하.
# 아이디어
    # 그래프로 표현하고, 각각 노드에서 자식 노드의 개수를 세주면서 적합 판단
# 시간복잡도
    # 그래프로 연결하고 BFS 탐색, n번 * n번 충분
# 변수계획
    # 개수 셀 count변수

n,m = list(map(int,input().split())) # 구슬 개수, 쌍의 개수
ans = 0
lightBoard = [[] for _ in range(n+1)]
heavyBoard = [[] for _ in range(n+1)] 
for _ in range(m):
    start,end = list(map(int,input().split()))
    lightBoard[start].append(end)
    heavyBoard[end].append(start)

def BFS (currNode,visited,board) :
    queue = deque()
    queue.append(currNode)
    visited[currNode] = True
    count = 0
    while queue:
        curr = queue.popleft()
        if len(board[curr]) > 0:
            for x in board[curr]:
                if visited[x] == False :
                    visited[x] = True
                    count += 1
                    queue.append(x)
    return count

for i in range(1,n+1):
    visited = [False] * (n+1)
    childs = BFS(i,visited,lightBoard)
    if childs >= (n+1)//2:
        ans += 1


    visited = [False] * (n+1)
    childs = BFS(i,visited,heavyBoard)
    if childs >= (n+1)//2:
        ans += 1

print(ans)

