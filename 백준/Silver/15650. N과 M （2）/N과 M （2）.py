import sys
import math
input = sys.stdin.readline

n,m = list(map(int,input().split()))
arr = [i for i in range(1,n+1)]
visited = [False] * (n+1)
# n개중에서 수열로 m개 고르기

def DFS (depth,ans,start) :
    if depth == m:
        ans.sort()
        print(' '.join(map(str,ans)))
        return
    for i in range(start,n+1):
        ans.append(i)
        DFS(depth+1,ans,i+1)
        ans.pop()
        

DFS(0,[],1)