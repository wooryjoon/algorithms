import sys
input = sys.stdin.readline
from collections import deque

# 트리의 특징
# 사이클이 없다.
# 정점이 n개. 간선이 n-1개
# 임의의 두 점에 대해 경로가 유일하다.
# while True :
#     n,m = (list(map(int,input().split()))) # 정점갯수,간선갯수
#     if n == 0 and m == 0 :
#         break
#     graph = [[] for _ in range(n+1)]
#     for _ in range(m) :
#         a,b = list(map(int,input().split()))
#         graph[a].append(b)
#         graph[b].append(a)

n,k = list(map(int,input().split()))
queue = deque()
ans = []
for i in range(1,n+1):
    queue.append(i)

while queue:
    for i in range(k):
        queue.append(queue.popleft())
    ans.append(queue.pop())
print('<' + ', '.join(map(str,ans)) + '>')