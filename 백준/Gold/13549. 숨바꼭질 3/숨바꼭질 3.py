# 걷는경우 : 1칸씩 이동
# 순간이동 : 두배씩 이동
# n = 수빈이 위치     m = 동생 위치
# n이 m을 찾는 가장 빠른 시간

from collections import deque

[n,m] = list(map(int,input().split()))
cases = [-1,1]
# 매 이동마다 걷기 / 순간이동 두개의 선택지가 존재한다 BFS로 각 경우를 체크
answer = []
def BFS (startNode) :
    queue = deque()
    queue.append([startNode,0]) # 0초에서 출발
    visited[startNode] = True
    while (queue):
        [currNode,time] = queue.popleft()
        if (currNode == m):
            return time
        movedNode = currNode * 2 # 곱하기2 먼저함.
        if (movedNode <= 100000 and movedNode >= 0 and visited[movedNode] ==False ):  # 아직 방문안한 지점이고 0보다크면
            queue.appendleft([movedNode,time])
            visited[movedNode] = True
        for i in range(2):
            movedNode = currNode + cases[i]
            if (movedNode <= 100000 and movedNode >= 0 and visited[movedNode] ==False):
                queue.append([movedNode,time+1])
                visited[movedNode] = True
visited = [False for _ in range(100001)]
print(BFS(n))

