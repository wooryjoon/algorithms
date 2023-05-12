def solution(n, computers):
    # 각 노드를 돌면서, DFS가 돌아가면 새 네트워크
    network = 0
    visited = [0] * n
    def DFS(currNode) :
        visited[currNode] = 1
        for i in range(len(computers[currNode])):
            if visited[i] : continue
            if computers[currNode][i] == 1 :
                DFS(i)
            
    for i in range(n):
        if visited[i] == 1 : continue
        network += 1
        DFS(i)
    return network