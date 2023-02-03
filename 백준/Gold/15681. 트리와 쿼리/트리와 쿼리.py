import sys
import copy
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(150000)
# 문제 정리
    # 트리구조 만들고, 어떤 정점의 서브트리 내의 정점의 수
# 아이디어

# 시간복잡도

# 변수계획


n,r,q = list(map(int,input().split()))
tree = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(n-1):
    start,end = list(map(int,input().split()))
    tree[start].append(end)
    tree[end].append(start)

def DFS (root) :
    visited[root] += 1
    for x in tree[root]:
        if visited[x] == 0:
            visited[root] += DFS(x)
    return visited[root]

DFS(r)
ans = []
for _ in range(q):
    ans.append(visited[int(input())])
print('\n'.join(map(str,ans)))