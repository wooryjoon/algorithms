from collections import deque
# 벽은 불에 전염이 안됨
# 상근이는 동서남북 이동 가능
# 상근이는 벽은 통과 못함
# 상근이는 불이붙은 칸이나, 이제 불이 붙으려는 칸에는 이동 못함.
# BFS를 돌리면서 불이번져나가는곳을 먼저 처리하고, 그다음에 상근이의 위치를 처리한다
# 중첩반복문을 통해서 BFS넣기전에 불난위치, 상근이 위치를 먼저 큐에 넣어준다.
# BFS함수 내에서, 큐에서 꺼낸게 불난위치이면 사방으로 불 번지게 하고
# 큐에서 꺼낸게 상근이 위치이면 사방으로 상근이 위치 번지게한다.
# 탈출조건 : 상근이 위치가 그래프 틀을 벗어나는 곳으로 가는 경우 -> 탈출!
# 근데 큐가 다 돌동안 상근이 위치가 내부에서만 멤도는 경우는  -> 임파써블
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS (Queue,row,col) :
    while (len(Queue)):
        [x,y,str,time] = Queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (str == '*'): # 해당 칸이 불이 있는 칸인 경우
                if (nx < 0 or ny < 0 or nx >= row or ny >= col
                or board[nx][ny] == '#' or board[nx][ny] =='*') : continue
                board[nx][ny] = '*' # 불번짐
                Queue.append([nx,ny,'*',time+1])
            elif (str == '@'): # 해당 칸이 사람이 있는 칸인 경우
                if (nx < 0 or ny < 0 or nx >= row or ny >= col) : # 탈출
                    print(time+1)
                    return
                elif (board[nx][ny] == '.'): # 이동가능
                    board[nx][ny] = '@'
                    Queue.append([nx,ny,'@',time+1])
    print("IMPOSSIBLE")
    return

t = int(input()) # 테스트케이스 갯수
for _ in range(t):
    queue = deque()
    y,x = map(int,input().split()) # 가로,세로 길이
    board = []

    for _ in range(x):
        board.append(list(input())) # board 생성
    
    for i in range(x):
        for j in range(y):
            if (board[i][j] == '*'):
                queue.append([i,j,'*',0]) # 보드에서 불난곳 먼저 푸쉬
    
    for i in range(x):
        for j in range(y):
            if (board[i][j] == '@'):
                    queue.append([i,j,'@',0]) # 보드에서 사람있는곳 푸쉬
    BFS(queue,x,y)
        
        