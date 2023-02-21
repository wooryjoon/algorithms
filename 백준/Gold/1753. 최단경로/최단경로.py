import sys
input = sys.stdin.readline
from heapq import heappush,heappop
# 우선순위큐를 사용한 다익스트라 알고맂ㅁ


V,E = list(map(int,input().split())) # 정점과 간선 개수
start = int(input())
graph = [[] for _ in range(V+1)] # 1부터V까지의 정점을 커버가능한 graph
table = [float('inf')] * (V+1)
for i in range(E):
    froms,end,worth = list(map(int,input().split()))
    graph[froms].append((end,worth)) # end로 가는데 worth가 든다.

def dijkstra (start) :
    table[start] = 0 # 출발지점은 0으로 초기화
    pq = []
    heappush(pq,(0,start)) # 우큐에 (비용,현재노드) 넣기.
    while pq :
        dist,curr = heappop(pq) # 힙에서 간선비용 최소인 (비용,노드) 꺼내기
        if table[curr] < dist:
            continue
        for x in graph[curr] :
            [nextNode,cost] = x # curr노드에서 다음노드까지의비용
            totalCost = table[curr] + cost # start에서 다음노드까지비용
            if table[nextNode] > totalCost :
                table[nextNode] = totalCost
                heappush(pq,(totalCost,nextNode))

dijkstra(start)
ans = []
for i in range(1,V+1):
    if table[i] <= 30000000:
        ans.append(str(table[i]))
    else :
        ans.append('INF')
print('\n'.join(ans))