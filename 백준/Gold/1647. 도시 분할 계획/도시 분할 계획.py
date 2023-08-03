from collections import deque
import sys
input = sys.stdin.readline


# 크루스칼 알고리즘
    # 1. 간선 정보 저장 후 오름차순 정렬
    # 2. 간선을 조회하며 서로 부모가 다르면 사이클이 아니므로 연결
    # 3. 서로의 부모를 같게 해줌

N,M = map(int,input().split())
info = []
ans = 0
for _ in range(M):
    # x,y,유지비
    a,b,c = map(int,input().split())
    info.append((c,a,b))
# 노드번호가 낮은 놈이 부모
parent = [i for i in range(0,N+1)]
def find_parent(node,parent):
    if parent[node] != node :
        parent[node] = find_parent(parent[node],parent)
    return parent[node]
def union(x,y,parent):
    x = find_parent(x,parent)
    y = find_parent(y,parent)

    if x < y :
        parent[y] = x
    else :
        parent[x] = y
# 간선 오름차순 정렬
info.sort()
# 간선 조회하며 연결 시작
maxx = -10
for e in info :
    cost,x,y = e
    if find_parent(x,parent) != find_parent(y,parent) :
            union(x,y,parent)
            ans += cost
            maxx = max(maxx,cost)

print(ans-maxx)

