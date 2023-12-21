from collections import deque
def solution(land):
    """
    [문제정리]
    시추관을 열을 뚫는다.
    통과한 칸과 연결된 모든 석유를 채취할 수 있다.
    어떤 열을 뚫어야 가장 많은 석유를 채취할 수 있는가?

    [InputSize]
    행,열 : 500
    [아이디어]
    1. 모든 열을 뚫어보며 max값 구한다.
    2. 연결된 석유칸은 전처리로 미리 연결된 모든 칸에 석유의 크기를 기록한다.
    3. 열을 뚫으며 석유칸에 써있는 값을 간단히 덧셈만 해주면 해결된다.
    [풀이방법]
    필요 변수 : max(정수)
    1. gasBoard에 석유칸 기록
    2. 모든 열을 순회하며 max값 갱신
    """
    def paintGasMap(board,row,col):
        dx = (0,0,1,-1)
        dy = (1,-1,0,0)
        visited = [[0] * col for _ in range(row)]
        
        def BFS(board,i,j,id):
            record = []
            q = deque()
            count = 1
            visited[i][j] = 1
            q.append((i,j))
            record.append((i,j))
            
            while q :
                x,y = q.popleft()
                
                for i in range(4):
                    nx,ny = x + dx[i], y + dy[i]
                    if 0<=nx<row and 0<=ny<col and visited[nx][ny] == 0:
                        if board[nx][ny] == 1 :
                            q.append((nx,ny))
                            visited[nx][ny] = 1
                            count += 1
                            record.append((nx,ny))
            for (x,y) in record :
                board[x][y] = [count,id]
                               
        id = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == 0 or visited[i][j] == 1 : continue
                else :
                    id += 1
                    BFS(board,i,j,id)
    answer = -1
    row = len(land)
    col = len(land[0])
    # 석유량 채우기
    paintGasMap(land,row,col)
    # # 모든 열 순회
    for i in range(col):
        amount = 0
        visited = set()
        for j in range(row):
            if land[j][i] == 0 : continue
            else :
                size,id = land[j][i]
                if id in visited : continue
                visited.add(id)
                amount += size
                
        answer = max(amount,answer)
    return answer