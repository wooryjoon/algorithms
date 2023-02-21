# 사방으로 이동  + 말처럼 이동 (K번)

from collections import deque

K = int(input()) # 말처럼 이동할 수 있는 횟수
[W,H] = list(map(int,input().split())) # W = 가로 H = 세로
board = [list(map(int,input().split())) for _ in range(H)] # 지도 완성
visited = [[[False for _ in range(K+1)] for _ in range(W)] for _ in range(H)]

# 사방으로 가는 경우의 수
dx = [0,0,1,-1]
dy = [1,-1,0,0]
# 말처럼 가는 경우의 수
kx = [-1,-2,-2,-1,1,2,2,1]
ky = [-2,-1,1,2,2,1,-1,-2]

# 기회

def BFS () :
    # 0,0에서 출발
    queue = deque()
    queue.append([0,0,0,0]) # 0,0 에서 출발하고, 0번의 이동 횟수 , 0번 말처럼 이동함
    visited[0][0][0] = True
    while(queue):
        [x,y,count,horseMove] = queue.popleft()
        if (x == H-1 and y == W-1): # 도착점에 도달한 경우
            return count
        if (horseMove < K): # 말처럼 움직일 수 있는 경우
            for i in range(8):
                nx = x + kx[i]
                ny = y + ky[i]
                # 말처럼 이동할 수 있는 다음 칸이 1. 범위내에 있고 2. 해당 층 지도에서 아직 방문 x
                if (0 <= nx < H and 0<= ny < W 
                and visited[nx][ny][horseMove+1] == False and board[nx][ny] == 0):
                    queue.append([nx,ny,count+1,horseMove+1])
                    visited[nx][ny][horseMove+1] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 양방향 다음칸이 1.범위내에 있고 2. 0이고 3. 아직 방문 안했으면
            if (0 <= nx < H and 0<= ny < W and board[nx][ny] == 0 
            and visited[nx][ny][horseMove] == False):
                queue.append([nx,ny,count+1,horseMove])
                visited[nx][ny][horseMove] = True
    return -1
    


print(BFS())
