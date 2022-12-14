from collections import deque
# 입력받고
N,M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input()))) # board 생성
def BFS () :
    queue = deque()
    queue.append([0,0,0]) # x y 찬스 사용여부
    visited[0][0][0] = 1
    while (len(queue)):
        [x,y,crashed] = queue.popleft()
        if (x == N-1 and y == M-1):
            return(visited[x][y][crashed])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx < 0 or ny < 0 or nx >= N or ny >= M):
                continue # 범위를 벗어나는 경우 
            if (board[nx][ny] == 0 and visited[nx][ny][crashed] == 0): # 벽이아니고,방문안한경우
                visited[nx][ny][crashed] = visited[x][y][crashed] + 1
                queue.append([nx,ny,crashed])
            elif (board[nx][ny] == 1 and visited[nx][ny][crashed] == 0): # 다음이 벽이고, 방문 안한경우
                if (crashed == 0): # 찬스 사용 안한경우
                    visited[nx][ny][1] = visited[x][y][crashed] + 1
                    queue.append([nx,ny,1])
                elif (crashed == 1): # 찬스 사용한 경우 
                    continue  
    return(-1)

#솔루션함수 만들고
def solution (N,M,board) :
    global visited,dx,dy
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)] # 삼차원배열의 첫항은 count, 두번째항은 
    #그 루트 상에서 crashed 찬스 썼는지 여부
    return BFS()

print(solution(N,M,board))