from collections import deque
T = int(input()) # 테스트케이스 개수
answer = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS (row,col) : 
    queue = deque([]);
    queue.append([row,col]);
    visited[row][col] = 0
    while (len(queue)):
        startNode = queue.popleft()
        for i in range(4):
            nx = startNode[0] + dx[i]
            ny = startNode[1] + dy[i]
            newNode = [nx,ny]
            if (nx < 0 or ny < 0 or nx >= M or ny >= N or visited[nx][ny] == 0): continue
            queue.append(newNode) 
            visited[nx][ny] = 0

for k in range(T):
    [M,N,K] = list(map(int,input().split())) #가로 : M 세로 : N 배추개수 : K
    visited = [];
    for i in range (M):
        col = []
        for j in range(N):
            col.append(0)
        visited.append(col) # map생성 왼료

    for i in range(K):
        row,col = list(map(int,input().split()))
        visited[row][col] = 1 # 배추 할당 완료
    count = 0;
    for i in range(M):
        for j in range(N):
            if (visited[i][j] == 1):
                count += 1;
                BFS(i,j)
    answer.append(count)
for i in range(len(answer)):
    print(answer[i])
    
