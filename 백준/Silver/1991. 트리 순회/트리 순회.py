import sys
import copy
from collections import deque
input = sys.stdin.readline
# 문제 정리
    # 1. DFS탐색
        # 왼쪽 우선, 그다음 오른쪽
    # 2. 왼쪽 - 부모 -오른쪽
        # 현재 노드에서 왼쪽이 없으면 append하고 부모로 이동
        # 부모append하고 오른쪽 이동, 오른쪽append
        # 
    # 3. 왼쪽 - 오른쪽 - 부모
# 아이디어
    # 각 원소마다 배열을 갖고, 인덱스0 : 왼쪽 인덱스1 : 오른쪽
# 시간복잡도

# 변수계획

n = int(input())
tree = {}
for i in range(1,n+1):
    root,left,right = list(input().split())
    tree[root] = [left,right] # [원소,[왼쪽자식,오른쪽자식]]

def preorder (tree,curr,ans) :
    ans.append(curr)
    for x in tree[curr]:
        if x =='.' : continue
        preorder(tree,x,ans)
    return ans

def inorder (tree,curr,ans) :
    if tree[curr][0] != '.':
        inorder(tree,tree[curr][0],ans)
    ans.append(curr)
    if tree[curr][1] !='.':
        inorder(tree,tree[curr][1],ans)
    return ans

def postorder (tree,curr,ans) :
    if tree[curr][0] != '.':
        postorder(tree,tree[curr][0],ans)
    if tree[curr][1] != '.':
        postorder(tree,tree[curr][1],ans)
    ans.append(curr)
    return ans

print(''.join(preorder(tree,'A',[])))
print(''.join(inorder(tree,'A',[])))
print(''.join(postorder(tree,'A',[])))