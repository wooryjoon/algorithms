import sys

input = sys.stdin.readline
from collections import deque

# 이분그래프 판별법 : 인접한 애들을 자기와 다른 색으로 채워나간다.
def BFS (graph,startNode,nodeColor) :
    nodeColor[startNode] = 1
    queue = deque()
    queue.append((startNode,1))
    
    while queue : 
        currNode,value = queue.popleft()
        for x in graph[currNode] :
            if nodeColor[x] == value : return False
            if nodeColor[x] == 0 :
                nodeColor[x] = -value
                queue.append((x,-value))
    return True

def sol () :
    ans = []
    K = int(input())
    for _ in range(K) :
        V,E = list(map(int,input().split())) # 정점 개수, 간선 개수
        graph = [[] for _ in range(V+1)] # 노드별 인접노드 배열 만들기
        nodeColor = [0] * (V+1)
        flag = True
        for _ in range(E) :
            u,v = list(map(int,input().split()))
            graph[u].append(v)
            graph[v].append(u)
        for i in range(1,V+1):
            if nodeColor[i] == 0 :
                flag = BFS(graph,i,nodeColor)
            if not flag : break
        if flag == True : ans.append('YES')
        else : ans.append('NO')
    return ans

print('\n'.join(sol()))


