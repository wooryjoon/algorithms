import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
dict = {}
ans = []
def DFS (depth,start) :
    if depth == m :
        temp = ' '.join(map(str,ans))
        if not dict.get(temp) :
            dict[temp] = 1
            print(temp)
        return
    for i in range(start,n):
        ans.append(arr[i])
        DFS(depth+1,i+1)
        ans.pop()


DFS(0,0)