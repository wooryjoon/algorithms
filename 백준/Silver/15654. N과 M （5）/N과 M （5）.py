import sys
import math
input = sys.stdin.readline

#1 2 3 4 중에 3개 고른다치면 1 1 2 가능
n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()

visited = [False] *(n)
# 순열
def DFS (depth,ans) :
    #종료조건
    if depth == m :
        print(' '.join(map(str,ans)))
        return
    for i in range(0,n):
        if visited[i] : continue
        visited[i] = True
        ans.append(arr[i])
        DFS(depth+1,ans)
        ans.pop()
        visited[i] = False

DFS(0,[])
