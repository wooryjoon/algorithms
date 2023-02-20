import sys
input = sys.stdin.readline

# v,e = list(map(int,input().split()))
# board = [list(map(int,input().split())) for _ in range(e)]
# parent = [0]*(v+1)
# result = 0

# for i in range(1,len(parent)):
#     parent[i] = i
# board.sort(key=lambda x:x[2])
# def find_parent(a) :
#     if parent[a] != a :
#         parent[a] = find_parent(parent[a])
#     return parent[a]
# def union_parent(a,b):
#     a = find_parent(a)
#     b = find_parent(b)
#     if a < b :
#         parent[b] = a
#     else:
#         parent[a] = b

# for edge in board :
#     [a,b,cost] = edge
#     if find_parent(a) != find_parent(b) :
#         union_parent(a,b)
#         result += cost
# print(result)

n,m = list(map(int,input().split())) # 1부터n까지 수중에 중복없이 1개 고른 수열
#permutation
visited = [0]*(n+1)
def DFS (depth,ans) :
    if depth == m :
        print(' '.join(ans))
        return
    for i in range(1,n+1):
        if visited[i] == 0 : # 아직 방문 안함
            ans.append(str(i))
            visited[i] = 1
            DFS(depth+1,ans)
            ans.pop()
            visited[i] = 0

DFS(0,[])