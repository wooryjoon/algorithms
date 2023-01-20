from collections import deque;

[n,m] = list(map(int,input().split()))
arr = [list(map(int,input().split())) for _ in range(m)] # 입력
mid = (n+1) // 2 # 중간 순서
heavyFirstTree = [[] for _ in range(n+1)]
lightFirstTree =  [[] for _ in range(n+1)]
ans = 0

for i in range(len(arr)):
    [start,to] = arr[i] # start가 to보다 무겁다
    heavyFirstTree[start].append(to)
    lightFirstTree[to].append(start)

def BFS(start,tree):
    queue = deque()
    visited[start] = True
    count = 0
    queue.append(start)
    while (len(queue)):
        currNode = queue.popleft()
        for e in tree[currNode]:
            if visited[e] == True:continue
            count += 1
            visited[e] = True
            queue.append(e)
    if n % 2 == 0: # 짝수개일때
        if count > mid : return 1  # 나가리
        else : return -1
    else: # 홀수개일때
        if count >= mid : return 1 # 나가리
        else : return -1
for i in range(1,n+1):
    visited = [False] * (n+1)
    a = BFS(i,heavyFirstTree)
    visited = [False] * (n+1)
    b = BFS(i,lightFirstTree)
    # 둘중 하나라도 나가리 판정 받았으면
    if (a == 1 or b == 1) : ans += 1
print(ans)