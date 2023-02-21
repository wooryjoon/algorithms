import sys
input = sys.stdin.readline
# 노드의 개수가 굉장히 작다.
# 간선, 간선비용
# A에서 B까지 가는 비용의 최소값 ? 2차원배열 DP로 처리가능

n = int(input())
m = int(input())
graph = [[float('inf')] *(n+1) for _ in range(n+1)] # inf로 초기화한 배열
for _ in range(m) :
    start,to,cost = list(map(int,input().split()))
    #start와 to가 같은 경우는 없다.
    graph[start][to] = min(graph[start][to],cost)

for i in range(1,n+1) :
    for j in range(1,n+1) :
        if i == j :
            graph[i][j] = 0
for k in range(1,n+1):
    for x in range(1,n+1):
        for y in range(1,n+1):
            graph[x][y] = min(graph[x][y],graph[x][k] + graph[k][y])
            

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] > 100000000:
            graph[i][j] = 0
    print(' '.join(map(str,graph[i][1:])))
        
            