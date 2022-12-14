from collections import deque


# T = 1
# size = [4]
# curr = [[3,2]]
# location = [[0,2]]
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


# BFS 로 칸마다 count 기록
def BFS (cx,cy,tx,ty) :
    queue = deque()
    board[cx][cy] = 1
    queue.append([cx,cy,1])
    while (len(queue)):
        [x,y,count] = queue.popleft()
        if (x == tx and y == ty) : 
            print(count-1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                nx < 0 or ny < 0 or nx >= L or ny >= L
            ) : continue
            if (board[nx][ny] == 0):
                board[nx][ny] = count + 1
                queue.append([nx,ny,count+1])
        
T = int(input())

for i in range(T) :
    L = int(input())
    board = [[0 for _ in range(L)] for _ in range(L)]
    cx,cy  = map(int,input().split())
    tx,ty =  map(int,input().split())
    # L = size[i]
    # board = [[0 for j in range(L)] for k in range(L)]
    # currNode = curr[i]
    # target = location[i]
    BFS(cx,cy,tx,ty)


