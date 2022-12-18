import sys
from collections import deque


# 0 - 1 bfs 탐색

def bfs():
    graph = [-1] * 100001
    graph[n] = 0
    queue = deque([n])

    while queue:
        target = queue.popleft()

        # 동생의 위치에 도달했다면 리턴
        if target == k:
            return graph[target]

        # 반복문을 통해 3가지 이동의 경우를 확인
        for i in (target + 1, target - 1, target * 2):

            # 이동하는 곳이 범위 내에 있고 이동하지 않았다면 이동
            if 0 <= i <= 100000 and graph[i] == -1:
                # 순간이동이라면
                if i == target * 2:
                    graph[i] = graph[target] # 0초 갱신
                    queue.appendleft(i) # 순간이동이기에 먼저 탐색

                else:
                    graph[i] = graph[target] + 1
                    queue.append(i)


n, k = map(int, sys.stdin.readline().split())
print(bfs())