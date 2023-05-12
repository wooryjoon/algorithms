from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    dx = (0,0,1,-1)
    dy = (1,-1,0,0)
    board = [[-1]*102 for _ in range(102)]
    for e in rectangle :
        y1,x1,y2,x2 = [i*2 for i in e]
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2 :
                    board[i][j] = 0
                elif board[i][j] != 0 :
                    board[i][j] = 1
    x,y = 2*characterY,2*characterX
    ix,iy = 2*itemY,2*itemX
    
    def BFS(i,j,ix,iy) :
        q = deque()
        q.append((i,j,0))
        board[i][j] = 0
        
        while q :
            x,y,dist = q.popleft()
            if x == ix and y == iy :
                return dist
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0<=nx<102 and 0<=ny<102 and board[nx][ny] == 1:
                    q.append((nx,ny,dist+1))
                    board[nx][ny] = 0
            
        
    return BFS(x,y,ix,iy) // 2
                          