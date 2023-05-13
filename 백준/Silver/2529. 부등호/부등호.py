import sys
input = sys.stdin.readline

# 최초 0~9 까지 모두 첫째 자리에 넣어보기 visited[x] 처리
# DFS(num,depth)
# if arr[depth] == '<' : 다음 수는 num보다 큰 애들이면서 unvisit애들로 DFS
# else : 다음 수는 num보다 작은 애들이면서 unvisit 애들로 DFS
k = int(input())
arr = list(input().split())
maxy = float('-inf')
miny = float('inf')
def fix (strings) :
    count = k+1 - len(strings)
    for _ in range(count):
        strings = '0' + strings
    return strings
def DFS(num,numStr,depth):
    global maxy
    global miny

    if depth == k :
        maxy = max(maxy,int(numStr))
        miny = min(miny,int(numStr))
        return

    if arr[depth] == '<':
        for i in range(num+1,10):
            if visited[i] == 1 : continue
            visited[i] = 1
            DFS(i,numStr+str(i),depth+1)
            visited[i] = 0

    elif arr[depth] == '>':
        for i in range(num):
            if visited[i] == 1 : continue
            visited[i] = 1
            DFS(i,numStr+str(i),depth+1)
            visited[i] = 0

for i in range(10):
    visited = [0]*10
    visited[i] = True
    DFS(i,str(i),0)

print(fix(str(maxy)))
print(fix(str(miny)))