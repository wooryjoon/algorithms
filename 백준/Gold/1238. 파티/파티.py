import sys
input = sys.stdin.readline
from heapq import heappush,heappop
# 우선순위큐를 사용한 다익스트라 알고리즘
# 각각의 start에서 다익스트라 돌리고, X까지의 최단거리 파악.
# 그리고 나서 X부터 start까지의 다익스트라

N,M,X = list(map(int,input().split()))# 사람수,간선수,도착지
graph = [[] for _ in range(M+1)]
ans = []
for _ in range(M):
    [start,end,worth] = list(map(int,input().split()))
    graph[start].append((end,worth)) # 목표노드와 거기까지의 거리

def dijkstra(start,to) :
    table = [float('inf')] *(N+1)
    pq = [] # 최단거리 담을 우선순위 큐
    table[start] = 0
    heappush(pq,(0,start)) # 초기 세팅
    while pq :
        dist,curr = heappop(pq)
        if table[curr] < dist :
            continue
        for x in graph[curr] :
            nextNode,cost = x
            totalCost = dist + cost
            if table[nextNode] > totalCost :
                table[nextNode] = totalCost
                heappush(pq,(totalCost,nextNode))
    return table[to]


for i in range(1,N+1):
    time = 0
    time += dijkstra(i,X)
    time += dijkstra(X,i)
    ans.append(time)
print(max(ans))